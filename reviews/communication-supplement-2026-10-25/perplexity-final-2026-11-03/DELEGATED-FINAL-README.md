# Communication Dzanga-Sangha — version finale consolidée pour Codex

Remise en fichiers : 3 novembre 2026.
État des preuves : lectures et tentatives consignées dans la conversation jusqu'au 2 novembre 2026 inclus.
Aucune nouvelle recherche web ni nouvelle lecture de source externe lors de cette remise.

## Ce qui est livré

- communication-supplement-verification-final.tsv : 64 entrées, dernier complément intégré.
- communication-supplement-verification-readme.md : bilan, réserves et transmission à Codex.

Ces deux fichiers remplacent, pour la transmission, le TSV complet antérieur ET son complément de cinq lignes. Il n'est plus nécessaire de juxtaposer ces anciens fichiers. La version présente incorpore SUP-24 vérifié, les trois autres lignes de blocage inchangées et l'alerte de discordance AMNH sur SUP-43.

Il s'agit d'une consolidation/reconstitution des résultats consignés, avec formulations synthétiques, pas d'une nouvelle campagne de vérification. Ne pas interpréter la date de remise comme date de consultation des sources.

## Bilan documentaire final

| Statut | Nombre |
|---|---:|
| verified_delegated | 35 |
| partial | 25 |
| blocked | 4 |
| duplicate_candidate | 0 |
| Total | 64 |

Les 64 entrées ont été examinées, mais ne sont PAS toutes intégralement confirmées. « Final » désigne la livraison du contrôle exécuté, non la résolution de chaque doute. verified_delegated qualifie l'identité et les métadonnées principales disponibles sur une source lue ; ce n'est ni validation scientifique, ni visionnage du film, ni certification de toutes les dates/éditions ou des droits.

## Registre et schéma

Registre exclusif d'identifiants : PERPLEXITY-VERIFICATION-PACKET-64.md, fourni par l'utilisateur. Les titres et autres déclarations du registre ne sont pas utilisés comme preuve externe de l'œuvre.

Six exclusions respectées : SUP-04, SUP-27, SUP-51, SUP-57, SUP-64 et SUP-65. Elles ne figurent pas dans le TSV et n'ont pas été rouverts.

Colonnes exactes, dans cet ordre :

id, status, title_confirmed, creator_confirmed, date_confirmed, type_confirmed, source_url, evidence_summary, dzanga_relevance, relationship_or_duplicate, limitations, checked_at.

Format : TSV UTF-8, en-tête puis 64 lignes, 12 colonnes. Les champs vides signifient non établi. Les informations secondaires sont qualifiées dans leur champ et/ou evidence_summary ; elles ne sont pas présentées comme une lecture de l'original.

checked_at = 2026-11-02 : date ISO 8601 du contrôle consigné. Le 3 novembre correspond uniquement à la génération de cette remise. Aucune précision horaire fictive.

source_url contient une URL effectivement appelée pendant les contrôles consignés. Pour une entrée blocked, c'est une tentative de lecture, PAS une page lue. Les URL complémentaires utiles figurent dans evidence_summary ; leur caractère partiel ou secondaire reste déclaré. Plusieurs sources en erreur n'ont pas de diagnostic HTTP précis : aucun paywall, absence ou suppression n'en est déduit.

## Dernier complément intégré

### SUP-24 — verified_delegated

https://www.newyorker.com/video/watch/notes-from-all-over-the-forest-elephants

Titre The Forest Elephants, série Notes from All Over. Résumé situant Andrea Turkalo au parc Dzanga-Ndoki/RCA et transcription substantielle réellement lus. Date affichée Released on 05/04/2015 conservée littéralement, sans imposer un format jour/mois non explicité. The New Yorker est l'éditeur ; Turkalo est intervenante/protagoniste, pas réalisatrice présumée. Vidéo non visionnée ; durée et réalisation/image/montage non affichés. Vidéo distincte de l'article SUP-23.

### SUP-43 — discordance AMNH, blocked maintenu

URL fournie : https://data.library.amnh.org/archives/repositories/3/archival_objects/25185

Candidat renvoyé par le moteur pour le titre D-20 Dzanga, Nov 28 1996 : https://data.library.amnh.org/archives/repositories/3/archival_objects/25180

Les notices, leur parent et l'index officiel n'ont pas été récupérés. Les indications du moteur restent search_excerpt_only. Aucun titre, support, identifiant d'objet ou date n'est confirmé sur cette base. Ne pas remplacer /25185 par /25180 automatiquement : mauvais lien initial, objets distincts ou autre relation restent possibles.

## Les quatre blocages

- SUP-42 : original NYT non récupéré. Des copies officielles du rapport WRI sont lisibles partiellement, sans atteindre la référence cible dans l'extraction. Métadonnées du moteur non promues ; aucune preuve du terrain APDS de l'article lue.
- SUP-43 : notices AMNH inaccessibles et discordance d'URL non résolue, comme détaillé ci-dessus.
- SUP-45 : archive CNN et voie officielle edition.cnn.com non récupérées. Aucun titre daté, signature, dateline ou média effectivement lu.
- SUP-58 : article BBC Earth News non récupéré, y compris miroir et chemin officiel alternatif. Films/clips BBC homonymes non utilisés comme substituts.

Les essais supplémentaires finaux n'ont pas apporté d'autre lecture primaire pour ces quatre cibles. Cela n'établit pas l'absence des documents.

## Correction territoriale importante — SUP-47

https://www.wrm.org.uy/bulletin-articles/logging-in-gabon-the-french-colonial-approach

Le texte ciblé est Logging in Gabon: the French colonial approach, WRM Bulletin15, 27 septembre1998. Le passage Gary Strieker/CNN Wild Planet, attribué en source finale à Giuseppe Vassallo/WEESA, porte sur Ipassa Mingouli, rivière Ivindo, au GABON. Il ne démontre pas un contenu APDS.

partial est conservé pour pertinence APDS non établie, malgré les métadonnées de l'article identifiées. La décision de conservation ou de classement reste humaine/Codex ; aucune suppression ou modification externe n'a été effectuée. Ne pas relier ce tournage à SUP-45 sans preuve.

## Les 25 entrées encore partielles

- SUP-01 — Film non visionné ; langues non établies ; affiche non récupérée ; 97 min propre à version IDFA, pas toutes éditions.
- SUP-02 — Aucune date depuis chemin URL ; restitution tronquée à la fin ; assertions attribuées, non validées.
- SUP-05 — Signature/date/crédits photographiques absents ; communiqué original non ouvert ; date URL non retenue.
- SUP-07 — Date éditoriale absente ; aucun podcast établi ; film intégré non visionné.
- SUP-08 — Sortie commerciale/durée/langues inconnues ; blog promotionnel ; aucun film/audio visionné ; commentaires non utilisés comme crédits.
- SUP-09 — Original/catalogue primaire non retrouvés ; année 1996 issue de sources tierces non retenue ; droits inconnus.
- SUP-10 — Film non visionné ; réalisation attestée par marchand, pas générique ; production unique et pertinence APDS primaire non résolues.
- SUP-12 — Dates/durées divergentes ; Zeyn réalisatrice non confirmée ; génériques non visionnés.
- SUP-15 — Contribution, auteur/pages/légende locale non retrouvés ; dépôt URL2021 non publication.
- SUP-17 — Film non visionné ; durée/générique inconnus ; pages24–25 rapportées seulement, non vérifiées.
- SUP-26 — 24mars2020 moteur seulement ; chiffres institutionnels attribués ; droits photos inconnus.
- SUP-36 — Date publication absente ; lien annexe Stephanie Markert non signature du récit ; médias non vus.
- SUP-38 — Auteur/pages/preuve APDS du bulletin inconnus ; contexte voisin insuffisant.
- SUP-39 — Date/durée/générique absents ; vidéos non vues ; exclusivité affichée, pas licence de rediffusion.
- SUP-40 — Date/signature personnelle absentes ; animation non vue ; durée/langue audio/droits inconnus.
- SUP-41 — Notice communautaire pas page de titre ; original non lu ; rapprochements HIS non audités.
- SUP-44 — 9octobre2020 non confirmé ; correction non substituée ; photos non vues ; résultats non validés.
- SUP-46 — Extraction limitée ; pagination non inventée ; reproduction sous conditions attribution/notification, pas licence inconditionnelle ; accusations attribuées.
- SUP-47 — Partial pour pertinence APDS manquante malgré métadonnées attestées ; décision conservation humaine ; film non vu.
- SUP-49 — Numérojanvier2005 moteur seulement, sommaire inaccessible ; aucune date confirmée ; corps sans signature initiale.
- SUP-56 — Pages/lieuBangui non validés ; période titre non année publication ; pas page de titre lue.
- SUP-66 — 1997/26min au moteur, absents des pages extraites, non promus primaire ; film non vu ; FauneSauvage inaccessible.
- SUP-67 — Année2010 non confirmée ; film/générique non vus ; droits universels indisponibles annoncés ; pas licence réutilisation.
- SUP-69 — Signature absente ; dates techniques pas en-tête complet ; dates2019 non confirmées ; médias non vus.
- SUP-70 — En-tête complet non restitué ; film/durée/langues inconnus ; ajout enquête2019-05 non publication originale.

## Doublons, traductions et éditions

Aucun candidat doublon entre identifiants SUP n'est suffisamment démontré pour duplicate_candidate. Aucune fusion décidée.

Relations conservées :
- SUP-01/41 : film inspiré du livre, œuvres distinctes.
- SUP-08 : fiction, dossier promotionnel, bande originale distincts ; manuscrit source nommé non assimilé à une édition particulière du livre.
- SUP-10 : durées Apple75/Prime52/Roku60/Blu-ray50 minutes et dates divergentes ; pas un montage unique présumé.
- SUP-11/12/13 : réalisateur/protagonistes/synopsis voisins insuffisants pour fusion ; lien des titres EN/FR de SUP-12 attesté, pas identité de toutes les versions.
- SUP-16 : index de SUP-06/21, pas nouvelle œuvre photographique.
- SUP-07/17 : film WCS évoqué, fichier non comparé ; rapport annuel distinct.
- SUP-20 : communiqué et présentation abrégée, distincts de l'étude scientifique.
- SUP-22 : même film identifié par titre/réalisateur/synopsis, versions79/52 minutes conservées sans identité de montage.
- SUP-23/24 : article et vidéo distincts ; SUP-24 désormais lisible mais non visionné.
- SUP-25/22 : article sur le film, pas édition du film.
- SUP-33 : GEO, relais HIOH et podcast distincts.
- SUP-34 : versions EN5mai2020 et ES13mai2020 correspondantes avec adaptations ; deux expressions séparées, pas identité mot-à-mot.
- SUP-38 : index distinct du bulletin individuel non récupéré.
- SUP-41 : Houghton Mifflin1993 distinct des autres éditions listées ; catalogue lu, pas livre.
- SUP-46/47/48 : recueil et contributions distincts ; SUP-47 concerne le Gabon.
- SUP-48/55 : WRM cite explicitement le reportage BBC et une autre source ; réécriture multisource distincte, pas doublon à fusionner.
- SUP-50 : relais ScienceDaily, communiqué institutionnel et étude distincts ; date7/8février originale contradictoire conservée.
- SUP-52/53 : même auteure et même date, articles distincts.
- SUP-60 : versions FR/EN correspondantes avec différence de répartition des armes, pas harmonisation silencieuse.
- SUP-63 : relais Changemakr attribué, pas seconde enquête démontrée.
- SUP-68/69 : pages/vidéo/articles linguistiques associés, identité complète montage/version non démontrée.

Les rapprochements MEDIA22/DEC22/DSC/HIS du registre restent seulement rapportés : les objets de ces services n'ont pas été ouverts pour décider une identité.

## Limites méthodologiques et droits

1. Aucune vidéo ou piste audio visionnée/écoutée. SUP-24 : transcription textuelle lue, pas vidéo.
2. Pages éditoriales, catalogues, références secondaires, index, dossiers promotionnels et textes primaires distingués dans evidence_summary.
3. Les PDF sont lus par extraction, parfois tronquée. Aucune pagination ou position PDF inventée ; passage non atteint = non lu.
4. Langue observée d'une page différente de langue explicitement cataloguée d'un film. Les éléments de langue/durée/pages restent dans les preuves sans modifier le schéma imposé.
5. Dates de publication, mise à jour, édition, production, diffusion, événement et tournage distinctes. Aucun jour depuis une année/saison, aucun copyright ou chemin URL traité comme publication.
6. Dates HIOH de SUP-30/31/33/37 attestées par des listes internes réellement lues, pas par un en-tête absent ; ce niveau est conservé.
7. Une simple mention de Dzanga ne prouve pas centrage APDS ; dzanga_relevance distingue contenu central, passage local, titre/référence et absence de preuve.
8. RCA, Congo-Brazzaville, RDC, Cameroun et Gabon distingués ; Nouabalé-Ndoki ne devient pas Dzanga-Ndoki.
9. Assertions scientifiques, accusations et témoignages attribués aux sources, sans validation indépendante.
10. Page accessible, vidéo visible et autorisation de réutilisation distinctes. Aucune licence générale inférée. Les conditions de reproduction WRM ne s'étendent pas indistinctement aux sources/images/films.
11. Aucun import, GitHub, Zotero, modification de dépôt, déploiement, achat, contact, Computer ou consultation d'une autre session Communication.
12. La présente remise n'a procédé à aucune nouvelle consultation des sources externes et ne redate pas les preuves.

## Transmission à Codex : priorités résiduelles

- Conserver les statuts et champs vides ; ne pas compléter depuis le seul registre ou moteur.
- Arbitrer la pertinence de SUP-47 et vérifier la discordance /25185-/25180 de SUP-43 par accès autorisé.
- Comparer génériques/montages pour SUP-10/11/12/13/22 avant toute décision d'identité.
- Obtenir les œuvres individuelles pour SUP-15/38/41/56 si déterminant ; ne pas convertir index/catalogue/citation en lecture du document.
- Maintenir les réserves de dates/signatures pour SUP-02/05/07/26/36/44/49/70.
- Contrôler les divergences FR/EN et référence juridique de SUP-60, sans fusion de versions.
- Ne pas promouvoir années/durées du moteur pour SUP-66/67 ni dates/versions incertaines de SUP-69.

Ce paquet livre un état de preuve documentaire ; il n'exécute ni n'autorise automatiquement une écriture, un import, une fusion ou un classement DSPA-Core.

## Contrôles techniques de cette remise

- Deux fichiers créés localement et vérifiés non vides.
- TSV UTF-8 : 64 identifiants uniques égaux au registre et 65 lignes physiques avec en-tête.
- 12 colonnes exactes, dans l'ordre demandé.
- Six exclusions absentes ; aucun identifiant supplémentaire.
- Statuts autorisés ; comptages35/25/4/0 cohérents.
- Complément SUP-24 et alerte AMNH intégrés dans le TSV complet, sans fichier de correctifs séparé nécessaire.

SHA-256 du TSV :
2719ab31a97e8e223b08c167278380c62b0044a7ff8a455dda4e2de5a2a5aba2
