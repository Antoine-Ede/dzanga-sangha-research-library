# Dzanga-Sangha Research Library

Site statique HTML/CSS/JavaScript alimenté en lecture par le [groupe Zotero 6701789](https://www.zotero.org/groups/6701789/dzanga-sangha_research_library/library). Zotero reste la source de vérité ; les instantanés dans `catalogue/` documentent les imports historiques.

## Développer et reprendre

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

## Architecture conservée

`index.html` charge `library-model.js`, `quality.js`, `analytics.js`, puis `app.js`. `app.js` lit les collections et notices Zotero avec pagination et présente recherche, filtres et trois vues. `analytics.js` analyse le corpus, `quality.js` prépare des vérifications, `library-model.js` centralise les catégories et conventions de tags. Le site est actuellement publié depuis `main` ; aucun déploiement n’est réalisé par les outils locaux de cette branche.

Les archives publiques et leurs manifestes restent dans [catalogue/apds-2026-10-08](catalogue/apds-2026-10-08/README.md). Les originaux et registres détaillés APDS restent hors du dépôt.
