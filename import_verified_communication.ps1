<#
Imports conservative, delegated-verified Communication webpages into Zotero.

Default mode is a read-only preflight.  Pass -Apply only after preflight is
clean.  The script never prints or writes ZOTERO_API_KEY, never deletes items,
and rechecks URL/title against the live group before each creation batch.
#>
[CmdletBinding()]
param([switch]$Apply)

$ErrorActionPreference = 'Stop'
$ExpectedGroupId = '6701789'
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$ManifestPath = Join-Path $Root 'reviews\communication-supplement-2026-10-25\communication-import-candidates.json'

function Stop-Safely([string]$Message) {
    Write-Output ('STOP: ' + $Message)
    exit 1
}

function Normalize-Url([string]$Value) {
    if ([string]::IsNullOrWhiteSpace($Value)) { return '' }
    return $Value.Trim().TrimEnd('/').ToLowerInvariant()
}

function Normalize-Title([string]$Value) {
    if ([string]::IsNullOrWhiteSpace($Value)) { return '' }
    return ([regex]::Replace($Value.ToLowerInvariant(), '[^\p{L}\p{N}]+', ''))
}

function Invoke-ZoteroRequest([string]$Method, [string]$Uri, [byte[]]$Body = $null, [hashtable]$AdditionalHeaders = @{}) {
    $headers = @{ 'Zotero-API-Key' = $env:ZOTERO_API_KEY }
    foreach ($name in $AdditionalHeaders.Keys) { $headers[$name] = $AdditionalHeaders[$name] }
    $params = @{ Method = $Method; Uri = $Uri; Headers = $headers; UseBasicParsing = $true; ErrorAction = 'Stop' }
    if ($null -ne $Body) { $params['Body'] = $Body; $params['ContentType'] = 'application/json; charset=utf-8' }
    return Invoke-WebRequest @params
}

function Read-ZoteroJson([string]$Uri) {
    $response = Invoke-ZoteroRequest -Method 'GET' -Uri $Uri
    return @{ response = $response; data = ($response.Content | ConvertFrom-Json) }
}

function Get-GroupPermissionState($Key) {
    # Current Zotero keys expose group permissions under access.groups, normally
    # with an `all` rule; retain the legacy shape only as a compatibility path.
    $scope = $null
    if ($null -ne $Key.access.groups) {
        $properties = @($Key.access.groups.psobject.Properties)
        $specific = $properties | Where-Object { $_.Name -eq $ExpectedGroupId } | Select-Object -First 1
        $all = $properties | Where-Object { $_.Name -eq 'all' } | Select-Object -First 1
        if ($null -ne $specific) { $scope = $specific.Value }
        elseif ($null -ne $all) { $scope = $all.Value }
    }
    if ($null -eq $scope -and $null -ne $Key.access.group) { $scope = $Key.access.group }
    if ($null -eq $scope) { return @{ read = $false; write = $false; schema = 'no-group-scope' } }
    $canRead = [bool]$scope.library -or [bool]$scope.read
    return @{ read = $canRead; write = [bool]$scope.write; schema = 'groups-scope' }
}

function Assert-Environment {
    if ([string]::IsNullOrWhiteSpace($env:ZOTERO_API_KEY)) { Stop-Safely 'ZOTERO_API_KEY is not loaded in this shell.' }
    if ($env:ZOTERO_GROUP_ID -ne $ExpectedGroupId) { Stop-Safely ('ZOTERO_GROUP_ID must equal ' + $ExpectedGroupId + '.') }
    $key = (Read-ZoteroJson 'https://api.zotero.org/keys/current').data
    $permission = Get-GroupPermissionState $key
    if (-not $permission.read -or -not $permission.write) { Stop-Safely 'Current Zotero key lacks group library/read and write permission.' }
    Write-Output 'Group read/write permissions: OK'
}

function Get-AllLiveItems {
    $items = New-Object System.Collections.Generic.List[object]
    $start = 0
    $version = $null
    while ($true) {
        $result = Read-ZoteroJson ("https://api.zotero.org/groups/$ExpectedGroupId/items?format=json&limit=100&start=$start")
        if ($null -eq $version) { $version = [string]$result.response.Headers['Last-Modified-Version'] }
        $page = @($result.data)
        foreach ($item in $page) { [void]$items.Add($item) }
        if ($page.Count -lt 100) { break }
        $start += $page.Count
    }
    return @{ items = $items; version = $version }
}

function Convert-CandidateToItem($Candidate) {
    $tags = @($Candidate.tags | ForEach-Object { @{ tag = [string]$_; type = 0 } })
    return @{
        itemType = 'webpage'
        title = [string]$Candidate.title
        creators = @($Candidate.creators)
        date = [string]$Candidate.date
        url = [string]$Candidate.url
        websiteTitle = [string]$Candidate.websiteTitle
        tags = $tags
        extra = [string]$Candidate.extra
    }
}

try {
    if (-not (Test-Path -LiteralPath $ManifestPath)) { Stop-Safely 'Communication import manifest is missing.' }
    $manifest = Get-Content -Raw -LiteralPath $ManifestPath -Encoding UTF8 | ConvertFrom-Json
    $candidates = @($manifest.candidates)
    if ($candidates.Count -ne [int]$manifest.candidate_count -or $candidates.Count -lt 1) { Stop-Safely 'Candidate manifest count assertion failed.' }
    $ids = @($candidates | ForEach-Object { [string]$_.id })
    if (($ids | Select-Object -Unique).Count -ne $ids.Count) { Stop-Safely 'Candidate manifest has duplicate IDs.' }
    foreach ($candidate in $candidates) {
        if ([string]::IsNullOrWhiteSpace([string]$candidate.title) -or [string]::IsNullOrWhiteSpace([string]$candidate.url)) { Stop-Safely ('Candidate ' + $candidate.id + ' lacks a title or URL.') }
        if ([string]$candidate.id -eq 'SUP-47') { Stop-Safely 'SUP-47 is explicitly excluded from Communication import.' }
    }
    Assert-Environment
    $live = Get-AllLiveItems
    $urlIndex = @{}; $titleIndex = @{}
    foreach ($item in $live.items) {
        if ($null -eq $item.data) { continue }
        $url = Normalize-Url ([string]$item.data.url)
        $title = Normalize-Title ([string]$item.data.title)
        if ($url) { $urlIndex[$url] = [string]$item.key }
        if ($title) { $titleIndex[$title] = [string]$item.key }
    }
    $pending = New-Object System.Collections.Generic.List[object]
    $already = New-Object System.Collections.Generic.List[object]
    foreach ($candidate in $candidates) {
        $url = Normalize-Url ([string]$candidate.url)
        $title = Normalize-Title ([string]$candidate.title)
        $match = $null; $basis = $null
        if ($urlIndex.ContainsKey($url)) { $match = $urlIndex[$url]; $basis = 'url' }
        elseif ($titleIndex.ContainsKey($title)) { $match = $titleIndex[$title]; $basis = 'normalized-title' }
        if ($null -ne $match) { [void]$already.Add([pscustomobject]@{ id = $candidate.id; key = $match; basis = $basis }) }
        else { [void]$pending.Add($candidate) }
    }
    Write-Output ("Communication candidates: {0}; already in Zotero: {1}; planned creations: {2}." -f $candidates.Count, $already.Count, $pending.Count)
    if (-not $Apply) { Write-Output 'Preflight only. Re-run with -Apply to create the planned records.'; exit 0 }
    $created = New-Object System.Collections.Generic.List[object]
    $failed = New-Object System.Collections.Generic.List[object]
    for ($offset = 0; $offset -lt $pending.Count; $offset += 25) {
        $last = [Math]::Min($offset + 24, $pending.Count - 1)
        $batch = @($pending[$offset..$last] | ForEach-Object { Convert-CandidateToItem $_ })
        # InputObject preserves an array even when the final batch contains one item
        # (Windows PowerShell 5.1 otherwise commonly serializes a scalar object).
        $json = ConvertTo-Json -InputObject $batch -Depth 12 -Compress
        if (-not $json.TrimStart().StartsWith('[')) { Stop-Safely 'Zotero batch payload is not a JSON array.' }
        $body = [System.Text.Encoding]::UTF8.GetBytes($json)
        $response = Invoke-ZoteroRequest -Method 'POST' -Uri "https://api.zotero.org/groups/$ExpectedGroupId/items" -Body $body -AdditionalHeaders @{ 'If-Unmodified-Since-Version' = $live.version }
        $result = $response.Content | ConvertFrom-Json
        if ($null -eq $result.successful) { Stop-Safely 'Zotero response lacks successful creation records.' }
        foreach ($property in $result.successful.psobject.Properties) {
            $index = [int]$property.Name; $key = [string]$property.Value
            $candidate = $pending[$offset + $index]
            $check = (Read-ZoteroJson "https://api.zotero.org/groups/$ExpectedGroupId/items/$key").data
            if ($check.data.title -ne $candidate.title -or (Normalize-Url $check.data.url) -ne (Normalize-Url $candidate.url)) { Stop-Safely ('Immediate Zotero verification failed for ' + $candidate.id + '.') }
            [void]$created.Add([pscustomobject]@{ id = $candidate.id; key = $key })
        }
        if ($null -ne $result.failed) {
            foreach ($property in $result.failed.psobject.Properties) { [void]$failed.Add([pscustomobject]@{ batchIndex = $property.Name; reason = 'Zotero reported failed creation.' }) }
        }
        $nextVersion = [string]$response.Headers['Last-Modified-Version']
        if ($nextVersion) { $live.version = $nextVersion }
    }
    if ($failed.Count -gt 0 -or $created.Count -ne $pending.Count) { Stop-Safely ('Import incomplete. Created=' + $created.Count + '; failures=' + $failed.Count + '.') }
    Write-Output ("Import complete. Created={0}; already present={1}; failures=0." -f $created.Count, $already.Count)
} catch {
    Stop-Safely $_.Exception.Message
}
