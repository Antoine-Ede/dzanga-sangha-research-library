"""Regression checks for Zotero group-permission preflight handling."""

from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "import_verified_communication.ps1"


def test_current_zotero_group_permission_schema_is_supported() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    assert "function Get-GroupPermissionState" in source
    assert "$Key.access.groups" in source
    assert "$scope.library" in source
    assert "$scope.write" in source


def test_legacy_group_permission_schema_remains_a_compatibility_path() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    assert "$Key.access.group" in source
    assert "Current Zotero key lacks group library/read and write permission." in source


def test_creation_response_uses_zotero_v3_item_key_not_object_text() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    assert "$property.Value.key" in source
    assert "Zotero v3 returns a creation object" in source
    assert "Created Communication record:" in source


def test_immediate_verification_normalizes_unicode_before_comparison() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    assert "NormalizationForm]::FormKC" in source
    assert "$titleMatches" in source
    assert "$urlMatches" in source
    assert "Immediate Zotero verification mismatch" in source
