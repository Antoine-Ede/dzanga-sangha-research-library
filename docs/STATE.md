# État vérifié — 15 octobre 2026

## Base et diagnostic

Base inspectée : `fbac9cd2cd81a06c6f3b1421a8cf225a4383b1bd`, identique à `origin/main` au démarrage. Dépôt distant : `Antoine-Ede/dzanga-sangha-research-library`. Checkout initial propre, PR APDS nº 1 fusionnée ; aucune PR ouverte observée. Travail actuel dans un worktree distinct, branche `codex/library-development-system`, sans upstream de publication. Une sauvegarde Git complète a été vérifiée avant sa création ; le checkout initial reste sur main.

Pas d’AGENTS, CLAUDE, tests versionnés, commande de contrôle ou CI métier à la base. GitHub ne présente que le déploiement Pages. La roadmap décrit correctement l’audit partiel mais mélangeait le prochain développement et le bilan historique.

Les scripts `curate_archive.py`, `archive_updates.py`, `text_audit.py`, `summarize_text_review.py`, `finalize_secondpass.py` et `verify_*` existent dans le dossier de travail parent, hors dépôt. Inspection du code seulement : pas de relance. Ils contiennent des chemins locaux, compteurs figés et, pour certains, anciennes URL de copies publiques. Ne pas les exécuter comme découverte générique. Réutilisation : conventions de tags, distinction proposition/application et test de rendu APDS ; aucun inventaire privé copié.

Écart observé : `Restricted-Original` est affiché par l’interface mais reste signalé comme accès à préciser par le modèle de qualité. Ce point reste dans ROADMAP ; il n’est pas corrigé dans ce lot sans décision sur la sémantique des deux accès.

## Mission locale livrée

Fiches : [lot 1](tasks/001-development.md), puis [lot 2](tasks/002-bibliography.md).
Rôles exercés successivement par la même session ; aucune revue indépendante déclarée.
Interdictions actuelles : écriture Zotero, push, publication, fusion et IA externe. Les chiffres APDS du bilan du 14 octobre sont historiques, pas un décompte actualisé du catalogue vivant.

## Validation et limites

Lot 1 réalisé et committé séparément : `45aa27c22ff175cd247e1d1e4cb45c5489e6e234`. Points d’entrée, documents, commande commune, scanner, preuve avec péremption, protection des artefacts APDS, test de rendu synthétique repris du travail existant. Preuve du lot isolé : `.local/lot1-verification.json` (historique, son SHA diffère du code actuel).

Lot 2 : CLI locale, normalisation et preuves par champ, instantané public Zotero versionné, découverte Crossref paginée, décisions avec historique, export JSON et sauvegarde SQLite. [Mode d’emploi](BIBLIOGRAPHY.md). Aucun fournisseur IA réel ; comparaison Pydantic AI / mode déterministe dans DECISIONS. Pas de hook, plateforme ou configuration globale ajoutés.

Le contrôle complet comprend 32 tests Python, syntaxe Python/JavaScript, rendu synthétique des trois vues, différences Git, données publiques historiques, empreintes des PDF inchangés, scanner de secrets/fichiers interdits et péremption des preuves. Les scénarios couvrent relance sans doublons, décisions conservées, métadonnées incomplètes, conflits, faux rapprochements, erreurs et reprises réseau simulées, catalogue changeant, absence d’IA, sauvegarde restaurable et refus des sorties prétendument validées. Résultat final, SHA complet et empreintes : `.local/verification.json` ; `./dev.ps1 check --verify-proof` doit réussir avant toute réutilisation. Les données ignorées sont hors de cette preuve.

Essai public distinct du 15 octobre : GET du groupe 6701789, version 946, 427 notices bibliographiques (428 éléments de premier niveau avant exclusion des notes/pièces non bibliographiques). Deux petites requêtes Crossref ont donné dix candidats conservés sans décision : cinq résultats larges bruités, puis cinq résultats ciblés sur le titre, dont quatre rapprochés du catalogue. Ces nombres décrivent cet essai, pas une constante du catalogue ni une sélection scientifiquement validée. Rapport local : `.local/public-smoke-report.json`, avec code et fichiers réellement éprouvés. Les exports publics de revue restent locaux.

Auto-revue critique : corrections sur les dates contradictoires, l’identité lors d’un DOI tardif, les titres avec guillemets/balises, la péremption après changement de catalogue et les pauses serveur, y compris lors d’un redémarrage. Aucune revue indépendante. Le site et les artefacts APDS restent inchangés : pas de test navigateur ni de publication revendiqués. Le scanner n’est pas une barrière complète ; le statut public d’une entrée reste une déclaration à vérifier humainement. Les tests ne prouvent ni la vérité des sources, ni la pertinence scientifique, ni les droits de diffusion.

## Reprise

Correctif local après essai dans le terminal utilisateur : les tests Python passaient, mais Node absent de PATH provoquait `FileNotFoundError`. Le lanceur Python cherche maintenant le runtime Node existant de Codex sous Windows après PATH, sans installation ni changement global. README donne aussi l’appel Python absolu depuis n’importe quel dossier lorsque `.ps1` est interdit. Deux tests de résolution ajoutés (34 tests au total) ; contrôle complet réussi avec Node retiré de PATH depuis le dossier utilisateur. La preuve finale et sa fraîcheur sont vérifiées sur le commit du correctif ; consulter son SHA dans .local/verification.json. L’échec utilisateur est conservé dans `.local/verification-user-node-missing.json`. Petit correctif limité à `tools/check.py`, ses tests et ces documents ; retour arrière par revert du correctif. Auto-revue, aucun changement du site ou des données. Le rapport public du lot 2 reste historique sur son SHA, pas une preuve de ce correctif.

Prochain petit lot recommandé : faire relire humainement les cinq candidats ciblés, vérifier les quatre rapprochements et consigner les décisions locales. Mesurer les sources/preuves manquantes avant d’ajouter un connecteur ou une interface. L’absence de couverture exhaustive des archives/thèses et l’absence de décision humaine réelle sont des limites ouvertes, pas un import à relancer. Toute écriture Zotero nécessitera une mission distincte autorisée.

Les futures sessions doivent relire ce document et la fiche applicable avant d’agir. Les registres APDS externes et leurs limites restent décrits dans ROADMAP ; cette mission n’a pas repris leur revue. Retour arrière : sauvegarder la base avec la commande `backup`, conserver les preuves puis revenir au checkout initial intact ; les deux commits locaux sont annulables séparément selon WORKFLOW. Ne pas supprimer `.local/` sans sauvegarde.
