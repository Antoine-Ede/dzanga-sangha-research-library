# Dzanga-Sangha Research Library

Site statique HTML/CSS/JavaScript alimenté en lecture par le [groupe Zotero 6701789](https://www.zotero.org/groups/6701789/dzanga-sangha_research_library/library). Zotero reste la source de vérité ; les instantanés dans `catalogue/` documentent les imports historiques.

## Développer et reprendre

L'onglet **Mode d'emploi** explique la consultation, l'accès aux PDF, l'ajout d'une référence et le classement ; lien direct `?section=help`. Les six copies publiques APDS préexistantes ont été [vérifiées sans connexion](docs/verification/public-plans-2026-10-16.json). L'accès à une copie expurgée ne modifie pas les conditions de consultation de l'original.

- [État vérifié et prochaine étape](docs/STATE.md)
- [Instructions Codex / Claude Code](AGENTS.md)
- [Procédure et preuves de contrôle](docs/WORKFLOW.md)
- [File bibliographique locale : essai et revue](docs/BIBLIOGRAPHY.md)
- [Décisions et raisons](docs/DECISIONS.md)
- [Priorités et audit APDS restant](ROADMAP.md)

Prérequis locaux : Python 3.11 ou plus récent, Node.js 18 ou plus récent et Git. Le site n’a pas de compilation ni de dépendance npm. Les outils déterministes utilisent la bibliothèque standard Python.

Depuis la racine :

```sh
python tools/check.py
python tools/check.py --verify-proof
```

La première commande exécute les contrôles hors ligne et écrit `.local/verification.json`. La seconde refuse une preuve échouée ou périmée. Ne pas committer `.local/`. Un checkout propre ne prouve pas qu’un contrôle a été exécuté.

Sous PowerShell, `./dev.ps1 check` et `./dev.ps1 check --verify-proof` sélectionnent Python disponible ou le runtime local fourni avec Codex si le raccourci Windows `python` est inutilisable. Aucune installation ni configuration globale. Les commandes Python ci-dessous et ce lanceur sont équivalents.

Si PowerShell refuse les scripts `.ps1`, appeler directement Python, sans changer la politique d’exécution. Cet exemple pour le worktree Windows fonctionne depuis n’importe quel dossier (adapter `$projet` si le dépôt a été déplacé) :

```powershell
$projet = Join-Path $env:USERPROFILE 'Documents\Codex\2026-10-08\github-plugin-github-openai-curated-remote\work\library-development-system'
$pythonExe = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $pythonExe "$projet\tools\check.py"
& $pythonExe "$projet\tools\check.py" --verify-proof
```

Le contrôle cherche Node.js dans PATH, puis, sous Windows, dans le runtime Codex déjà présent dans le profil utilisateur. Il consigne le chemin exécuté et sa version dans la preuve. Si aucun runtime n’est disponible, il échoue explicitement ; aucun téléchargement ni changement de PATH global. Une preuve échouée est refusée par `--verify-proof` : c’est le comportement attendu jusqu’à la réussite d’un nouveau contrôle.

## Architecture conservée

`index.html` charge `library-model.js`, `quality.js`, `analytics.js`, puis `app.js`. `app.js` lit les collections et notices Zotero avec pagination et présente recherche, filtres et trois vues. `analytics.js` analyse le corpus, `quality.js` prépare des vérifications, `library-model.js` centralise les catégories et conventions de tags. Le site est actuellement publié depuis `main` ; aucun déploiement n’est réalisé par les outils locaux de cette branche.

Les archives publiques et leurs manifestes restent dans [catalogue/apds-2026-10-08](catalogue/apds-2026-10-08/README.md). Les originaux et registres détaillés APDS restent hors du dépôt.
