# Supplément Communication — réception du 25 octobre 2026

Les **70 entrées SUP-01 à SUP-70** complètent les 60 pistes DSC et les entités HIS ; elles ne les remplacent pas. Elles incluent familles, versions, articles, objets d'archives et index, et ne représentent pas 70 œuvres nouvelles.

## Conservation et provenance

- [Registre déclaré](reported-sources.tsv) : titres, dates, responsabilités/langues, liens, réserves, lignes source et blocs conservés exactement dans une chaîne JSON. Toutes les lignes restent au statut conversation_reported.
- [Liens multiples](reported-links.tsv) : une ligne par lien fourni, sans attestation d'accès ni de redirection.
- [Empreinte du document reçu](provenance.json) : fichier utilisateur, taille et SHA-256 ; original intégral privé sous .local/perplexity-handoffs/COMM-EXTERNAL/.
- [Premier registre](../communication-discovery-2026-10-24/README.md) : 60 pistes conservées et première revue documentée ; aucune donnée écrasée.

La passation compile des résultats d'une autre conversation. « Consulté » y décrit un travail rapporté, pas une consultation par Codex dans cette session. Ses propositions de commandes ou d'actions ne créent pas d'autorisation supplémentaire. Les limites des registres antérieurs et les résultats du 24/25 octobre restent datés, sans être invalidés par une déclaration plus ancienne du supplément.

Les liens à DSC-040, DSC-051, DSC-013, DSC-055 et DSC-043 sont des enrichissements rapportés, pas des fusions exécutées. SUP-41 renvoie au livre Sarno, distinct du film SUP-01 et du Bayaka de DSC-050. La correspondance d'édition reste à vérifier.

## Limites et suite

Premier commit : conservation seulement, zéro vérification web nouvelle. Le rapprochement hors ligne devra distinguer lien exact, candidat par titre et relation documentaire, sans appeler ces rapprochements des sources validées. Aucun total d'œuvres nouvelles ne peut être déduit de 60 + 70.

Les vidéos exclusives pour adoptants (SUP-39) ne sont pas téléchargées. Le bulletin public APDS (SUP-60) est enregistré comme piste, sans reprise de l'audit d'archives réservé à l'autre session. Index, traductions, versions courtes/longues, œuvres et composantes restent distincts. Aucune fiction n'est transformée en documentaire par son seul sujet.

Toutes les recherches web supplémentaires passent par Perplexity. Aucun import Zotero, push, fusion ni déploiement sans nouvel accord. La session Communication externe n'a pas été consultée ou modifiée : seul le fichier transmis est traité. Auto-revue de la même session, pas de revue indépendante revendiquée.

## Rapprochement hors ligne terminé

Voir le [bilan et ses limites](RECONCILIATION.md). Sept correspondances d'URL dans l'instantané Zotero du 24 octobre, 63 sans correspondance exacte selon cette méthode, 12 entrées avec candidats dans les registres locaux, cinq enrichissements DSC rapportés. Aucun de ces compteurs n'est un nombre d'œuvres nouvelles ou une décision de doublon. [File de revue](review-queue.tsv), [alertes](review-alerts.tsv). Toutes les entrées source conservent leur statut conversation_reported ; aucun accès web nouveau.

## Vérifications prioritaires consolidées le 29 octobre

[Résultats et limites des six cas](PRIORITY-REVIEW.md) : une confirmation déléguée, quatre partiels, un blocage. Consultations Perplexity du 25 octobre, sans nouvelle lecture de source lors de la consolidation. Les alertes de date restent ouvertes ; les états de réception et rapprochement ci-dessus sont historiques. Aucun import ou déploiement.

## Livraison finale déléguée reçue le 4 novembre

La remise de 64 entrées hors six dossiers déjà consolidés est conservée dans [`perplexity-final-2026-11-03/`](perplexity-final-2026-11-03/). Son [intégration et ses limites](perplexity-final-2026-11-03/INTEGRATION.md) distinguent explicitement les assertions de lecture rapportées de toute vérification indépendante par Codex. Le contrôle local confirme l'ensemble exact des identifiants, le schéma et les statuts : 35 `verified_delegated`, 25 `partial`, 4 `blocked`. Aucun import Zotero, rapprochement automatique, push ou déploiement.
