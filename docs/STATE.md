# État vérifié — 15 octobre 2026

## Base et diagnostic

Base inspectée : `fbac9cd2cd81a06c6f3b1421a8cf225a4383b1bd`, identique à `origin/main` au démarrage. Dépôt distant : `Antoine-Ede/dzanga-sangha-research-library`. Checkout initial propre, PR APDS nº 1 fusionnée ; aucune PR ouverte observée. Travail actuel dans un worktree distinct, branche `codex/library-development-system`, sans upstream de publication. Une sauvegarde Git complète a été vérifiée avant sa création ; le checkout initial reste sur main.

Pas d’AGENTS, CLAUDE, tests versionnés, commande de contrôle ou CI métier à la base. GitHub ne présente que le déploiement Pages. La roadmap décrit correctement l’audit partiel mais mélangeait le prochain développement et le bilan historique.

Les scripts `curate_archive.py`, `archive_updates.py`, `text_audit.py`, `summarize_text_review.py`, `finalize_secondpass.py` et `verify_*` existent dans le dossier de travail parent, hors dépôt. Inspection du code seulement : pas de relance. Ils contiennent des chemins locaux, compteurs figés et, pour certains, anciennes URL de copies publiques. Ne pas les exécuter comme découverte générique. Réutilisation : conventions de tags, distinction proposition/application et test de rendu APDS ; aucun inventaire privé copié.

Écart observé : `Restricted-Original` est affiché par l’interface mais reste signalé comme accès à préciser par le modèle de qualité. Ce point reste dans ROADMAP ; il n’est pas corrigé dans ce lot sans décision sur la sémantique des deux accès.

## Mission active

Fiches : [lot 1](tasks/001-development.md), puis [lot 2](tasks/002-bibliography.md).
Rôles exercés successivement par la même session ; aucune revue indépendante déclarée.
Interdictions actuelles : écriture Zotero, push, publication, fusion et IA externe. Les chiffres APDS du bilan du 14 octobre sont historiques, pas un décompte actualisé du catalogue vivant.

## Validation et limites

Lot 1 réalisé : points d’entrée, documents, commande commune, scanner, preuve avec péremption, protection des artefacts APDS, test de rendu synthétique repris du travail existant. Premier passage réussi après adaptation aux fins de ligne Git et au runtime Python Windows. Résultats finaux et empreintes : `.local/verification.json` après contrôle de l’état final ; `--verify-proof` doit réussir avant de réutiliser une preuve. La revue critique est une auto-revue, pas une revue indépendante.

## Reprise

Prochaine étape : prototype CLI du lot 2. Les futures sessions doivent relire ce document et la fiche active avant d’agir. Les registres APDS externes et leurs limites restent décrits dans ROADMAP ; cette mission ne reprend pas leur revue.
