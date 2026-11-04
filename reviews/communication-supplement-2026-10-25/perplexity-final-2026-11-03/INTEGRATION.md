# Livraison déléguée Perplexity — intégration documentaire

Le responsable a transmis ces deux fichiers à Codex le 4 novembre 2026 :

- `delegated-final-review.tsv`, SHA-256 `2719ab31a97e8e223b08c167278380c62b0044a7ff8a455dda4e2de5a2a5aba2` ;
- `DELEGATED-FINAL-README.md`, SHA-256 `e5ca3f26a01a7276a2f01b513e6a67b390011abf8810c52a8107ad173fe7fcc5`.

Le TSV est une livraison Perplexity, reçue via le responsable : ses mentions `*_read`, ses URL et ses interprétations sont des **assertions déléguées**, pas une relecture indépendante des sources par Codex. Les données sources initiales dans `reported-sources.tsv` restent `conversation_reported` et ne sont pas écrasées.

## Contrôle local de réception

Le validateur fail-closed `tools/validate_perplexity_final.py` confirme : 64 lignes, 64 identifiants uniques, exactement l'ensemble SUP attendu hors SUP-04, SUP-27, SUP-51, SUP-57, SUP-64 et SUP-65 ; 12 colonnes dans l'ordre prescrit ; URL et date ISO présentes ; aucun statut hors schéma.

Les statuts livrés sont : 35 `verified_delegated`, 25 `partial`, 4 `blocked` et aucun `duplicate_candidate`. Ils décrivent le niveau de preuve rapporté, jamais une décision d'import, de fusion, de droits, d'accès public ou de classement DSPA-Core.

## Portée et limites

La livraison indique que ses dernières consultations remontent au 2 novembre et que la remise a été produite le 3 novembre. Codex l'a reçue le 4 novembre, sans appeler aucune URL. Le statut `verified_delegated` n'atteste donc pas une lecture primaire indépendante, un visionnage/écoute, une validation scientifique, ni une vérification actuelle des droits.

Les six dossiers exclus restent régis par `PRIORITY-REVIEW.md` et ne sont pas remplacés. Les rapprochements DSC, HIS, MEDIA22 et DEC22 demeurent des candidats ; aucune fusion n'est exécutée. Les quatre blocages signalés (SUP-42, SUP-43, SUP-45, SUP-58) restent ouverts. La conservation de SUP-47, qui ne prouve pas une pertinence APDS, est une décision humaine à venir.

Aucun import Zotero, aucune écriture dans le catalogue, aucun push, aucune fusion et aucun déploiement ne sont réalisés par cette intégration documentaire.
