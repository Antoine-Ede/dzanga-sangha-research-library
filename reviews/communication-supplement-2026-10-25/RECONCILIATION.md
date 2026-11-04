# Rapprochement du supplément — 25 octobre 2026

Premier commit de conservation : **6c581e7e48a131568fe72cc480e0ece84fc2b399**. Les 70 blocs et 101 liens rapportés sont préservés ; aucune source du supplément n'est nouvellement déclarée vérifiée.

## Ce qui a été comparé

Rapprochement strictement hors ligne avec les registres DSC/HIS, les 23 notices et décisions médiatiques du 22 octobre et l'instantané Zotero complet sauvegardé le **24 octobre à 19:12 UTC**, version 1017 : cinq pages, 459 objets dont 458 références. [Provenance de l'instantané](snapshot-provenance.json). Ce n'est pas une interrogation actuelle du groupe.

[70 résultats de rapprochement](snapshot-matches.tsv), [détails des sept candidats](snapshot-candidates.json), [relations locales](local-relations.tsv), [relations internes provisoires](within-supplement-relations.tsv), [file de revue](review-queue.tsv), [bilan calculé](reconciliation-summary.json).

## Résultats calculés

- **7 entrées avec correspondance d'URL dans l'instantané** : SUP-04, SUP-05, SUP-27, SUP-28, SUP-57, SUP-61, SUP-62. Les clés identifient les notices observées à la date de l'instantané, pas une validation du document ni une nouvelle création.
- **63 sans correspondance exacte URL/titre** par cette méthode. Cela ne prouve pas leur absence : traductions, migrations de liens, versions, titres abrégés et notices bibliographiques restent à examiner.
- **12 entrées avec candidats URL/titre dans les registres locaux** : résultat distinct des correspondances Zotero ; les décisions du 22 octobre peuvent déjà mentionner une piste non importée.
- **5 enrichissements DSC explicitement rapportés** : SUP-33, SUP-64, SUP-65, SUP-66, SUP-68. Ce sont des liens documentaires, pas cinq doublons démontrés.
- SUP-41 est rapproché du livre Sarno HIS-001/HIS-010 comme famille d'éditions à confirmer. SUP-01 est un film homonyme distinct ; pas de fusion sur titre.
- **Zéro source nouvellement vérifiée, zéro import, zéro modification Zotero.** Aucun dénombrement d'œuvres nouvelles n'est déduit de ces 70 entrées.

Une même URL peut servir à citer une autre œuvre : SUP-56, SUP-64 et autres références secondaires ne deviennent pas leurs documents cités. Les correspondances avec un recueil, une notice ou un index ne suffisent pas à identifier un article ou un épisode.

## Alertes et priorités

Les [sept alertes de revue](review-alerts.tsv) conservent les discordances sans correction automatique : date El País SUP-04, date saisonnière de SUP-27, année du bulletin SUP-57, niveau de preuve du film SUP-66, page/clip DW SUP-68, critique Kirkus de 1992 déjà documentée et liens associés de SUP-33.

Prochaine vérification utile, via Perplexity uniquement : SUP-65 (PDF CARPO et version web de l'entretien déjà connu), SUP-64 (référence National Geographic et terrain), SUP-51 (presse de 1994), puis les alertes de dates. Les films à durées divergentes (SUP-10 à SUP-13, SUP-22, SUP-67 à SUP-69) nécessitent des génériques et une distinction des montages ; plusieurs pages de plateforme ne créent pas plusieurs films.

Trois entrées sont des outils de repérage (SUP-16, SUP-29, SUP-38), SUP-32 regroupe des pages institutionnelles évolutives. SUP-39 nécessite une revue de métadonnées sans télécharger les médias exclusifs. SUP-60 est un bulletin public enregistré comme piste ; le traitement des archives APDS reste réservé à l'autre session.

## Livraison et limites

Les titres, dates, rôles et langues du supplément restent dans des colonnes rapportées. Les relations sont des candidats, des rapprochements déclarés ou des hypothèses explicites, jamais des fusions. La base DSC/HIS et ses résultats sont inchangés. L'original intégral et les traces de réception restent privés avec empreinte ; aucun fichier de la session externe n'a été consulté directement.

Aucune nouvelle recherche web, aucun import Zotero, push, fusion ou déploiement dans cette réception. Auto-revue de la même session ; pas de relecteur indépendant. Retour arrière : retirer le commit de rapprochement sans retirer la première conservation, en préservant le Markdown privé et les anciens registres.

## Vérifications prioritaires consolidées le 29 octobre

[Résultats et limites des six cas](PRIORITY-REVIEW.md) : une confirmation déléguée, quatre partiels, un blocage. Consultations Perplexity du 25 octobre, sans nouvelle lecture de source lors de la consolidation. Les alertes de date restent ouvertes ; les états de réception et rapprochement ci-dessus sont historiques. Aucun import ou déploiement.
