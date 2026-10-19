# Suivi du projet et reprise de l’audit APDS

## État courant — 19 octobre 2026

- [Lot 014](docs/tasks/014-author-copies.md) : propre notice de thèse Goldsmith retrouvée, URL réparée ; accès indéterminé conservé. Compteur **124/435 inchangé**, liens manquants hors archives 3 → 2. Restent onze accès, deux URL de thèses et une date FTNS. [Bilan des pistes et limites](reviews/author-copies-2026-10-19/README.md). Priorité aux preuves des auteurs/organismes ; ne pas répéter les mêmes recherches sans piste nouvelle. Archives APDS réservées à l'autre session.

- Suite [lot 013](docs/tasks/013-quality-followup.md) : trois corrections, deux textes gratuits confirmés et organisme AfESG identifié ; relance zéro écriture. Compteur **124/435**, dont 110 archives réservées et [14 incertitudes hors archives](reviews/quality-followup-2026-10-19/remaining-nonarchive.csv). Aucun import, règles inchangées ; [bilan et preuves](reviews/quality-followup-2026-10-19/README.md).

## Livraisons précédentes — 17 octobre 2026

- Revue qualité [lot 012](docs/tasks/012-quality-review.md) terminée pour le tri de 144 alertes et les 34 notices hors archives : 23 corrigées, compteur réel **127/435** avec les mêmes règles. Restent 110 archives pour l'autre session et [17 incertitudes documentées](reviews/quality-2026-10-17/remaining-nonarchive.csv). Aucun import ni scan APDS ; sauvegarde, lecture publique et relance sans écriture contrôlées.
- PR 4 livrée sur Pages : lien PDF et pilote Bayanga terminés, ne pas les rejouer. PR 5 fusionnée : bilan PubMed consigné, huit notices déjà importées. PR 6 fusionnée et publiée sur Pages le 17 octobre : Mode d'emploi accessible. Preuves du [lot 009](docs/tasks/009-integration-reconciliation.md) dans STATE.
- Les six copies APDS publiques sont accessibles sans connexion et conformes au manifeste (contrôle du 16 octobre). Cela ne rend pas les autres originaux diffusables.
- L'audit APDS continuera dans l'autre session : le responsable précise que les registres sont sur l'autre ordinateur, après avoir initialement demandé le transfert ici. Aucun compteur ni décision réinitialisé et aucune nouvelle page auditée dans cette session.
- MCCPAMU3 corrigée et relance sans écriture vérifiée : treize auteurs et titre, sans toucher aux classifications ([lot 010](docs/tasks/010-source-closeout.md)). Le point Flahou est résolu : téléchargements institutionnels confirmés, URL PDF et accès gratuit dans Zotero, lien du hub vérifié dans les trois vues ([lot 011](docs/tasks/011-flahou-fulltext.md)). Restent distincts : audit APDS dans l'autre session, sources historiques/communautaires et future veille non activée.

Les paragraphes datés du 15/16 octobre ci-dessous sont l'historique de cadrage ; leurs formules « prochain lot », « localement » et « pas encore » ne remplacent pas cet état courant. Les chiffres des anciens audits ne sont pas présentés comme de nouveaux contrôles.

## Priorité actuelle — système local de développement et propositions

Mission initiale du 15 octobre : [socle de développement](docs/tasks/001-development.md), puis [file bibliographique locale](docs/tasks/002-bibliography.md). L'utilisateur a ensuite autorisé la fusion à main au moment opportun : [intégration et suites](docs/tasks/004-integration-and-follow-up.md). État vérifié : [STATE](docs/STATE.md). Aucun import Zotero ni lancement planifié dans ce lot ; valider le parcours manuel avant toute IA réelle ou automatisation.

Les deux lots locaux et le premier tri de dix candidats sont réalisés : une référence contextuelle retenue avec accord utilisateur, quatre doublons d’instantané et cinq résultats hors périmètre identifiés par l’assistant. Exports et limites dans STATE ; aucune écriture Zotero. La couverture sans DOI, les nouvelles sources et la qualité des preuves restent à évaluer avant tout connecteur supplémentaire, interface ou fournisseur IA. Le prototype distingue la décision humaine du tri assistant, actuellement exporté séparément ; envisager son intégration native uniquement si le parcours se répète. Les chiffres APDS ci-dessous restent un bilan historique préservé.

## Demandes du responsable — suites priorisées du 15 octobre 2026

Point actuel du 16 octobre : lot 005 livré par PR nº 3. [Lot 006](docs/tasks/006-pdf-access.md) prépare localement le lien PDF explicite dans les trois vues. Le téléchargement anonyme de la copie expurgée Bayanga est vérifié (empreinte identique au manifeste). Copie expurgée stockée dans Zotero (CM5RDMRW), retéléchargement authentifié conforme ; accès anonyme Zotero en 404, donc URL publique complémentaire conservée. Intégration autorisée par le responsable ; résultat de livraison et contrôles dans `.local/pdf-access-delivery.json`. Ce pilote ne généralise pas l'accès à tous les scans APDS ni aux pièces jointes réservées aux membres. Les priorités ci-dessous restent suivies.

Ces évolutions sont cadrées, **pas encore implémentées**. La fusion du socle ne les rend pas disponibles.

Actualisation du 16 octobre : [lot 005](docs/tasks/005-notice-quality.md) réalise le résumé compact des archives et le signalement des noms suspects. Tests navigateur ajoutés au contrôle commun ; aperçu accepté par le responsable, intégration après contrôle final. Correction des treize auteurs préparée séparément, non appliquée. La prochaine priorité est le pilote PDF accessible depuis le site avec lien distinct de la notice : le code actuel n'exploite que DOI/URL, pas les pièces jointes Zotero. Les autres suites ci-dessous restent ouvertes. Audit APDS inchangé au lot 20 : cette amélioration d'interface ne compte aucune page supplémentaire.

1. **Tri APDS proportionné**, décision active [D005](docs/DECISIONS.md) : cesser d'imposer la lecture visuelle de toutes les pages pour le tri initial. Examiner identité, nature, OCR et passages ciblés ; approfondir les alertes et la mauvaise reconnaissance. Suivre séparément tri documentaire et pages effectivement relues. Préserver droits, originaux et expurgations existantes.
2. **Auteurs et notices lisibles — prochain petit lot recommandé.** Exemple vérifié par GET : notice `MCCPAMU3`, DOI `10.1111/eva.12075`, les treize créateurs ont des initiales dans `lastName` et les patronymes dans `firstName`. Le filtre utilise le nom de famille et affiche donc « A » ; [PubMed](https://pubmed.ncbi.nlm.nih.gov/24062800/) confirme notamment J Pinto et A Egyir-Yawson. Préparer une correction sourcée dans Zotero, avec sauvegarde et comparaison de version, sans inversion automatique de tout le catalogue ni développement de prénoms inconnus. Signaler les autres anomalies à examiner ; préserver auteurs institutionnels et vrais noms courts. Vérifier aussi les espaces parasites du titre « A frican / A nopheles ». Critère : filtre par patronyme correct, sans perte des créateurs, après validation de la correction.

   Pour l'exemple APDS-019, `archiveInfo()` affiche tout `extra` à partir de « Copie conservée » ; les paragraphes de conservation et la vérification d'accès en anglais se répètent sémantiquement. Prévoir un résumé français compact : provenance, lacunes exactes, accès à l'original, accès au PDF ; détails consultables à la demande. Préserver les preuves complètes dans Zotero et les avertissements utiles, sans simple suppression globale du texte. Absence de DOI seule ≠ défaut bloquant de notice. Tester cartes/liste/tableau, clavier et lecteur d'écran.
3. **PDF APDS sans DOI conservés dans Zotero et accessibles depuis Pages.** Pour chaque candidat approprié : pièce jointe à la notice existante, empreinte et version (original/copie expurgée) identifiées, sans recréer la notice. Préférer une version complète en ligne vérifiée lorsqu'elle existe, avec provenance APDS conservée. Pilote sur un document à risque faible et droits clarifiés : accès depuis un navigateur non connecté, lien durable, téléchargement correct, aucun secret exposé, taille/quota vérifiés. Le groupe est `PublicClosed`, lecture publique et édition de fichiers membres activées au GET du 15 octobre. [Zotero décrit un partage des fichiers entre membres](https://www.zotero.org/support/groups) : stockage dans le groupe ne garantit pas téléchargement anonyme. Si celui-ci n'est pas possible, proposer un dépôt public durable autorisé en complément de Zotero. Ne pas promettre un hébergement illimité gratuit ni remplacer les originaux sensibles par des copies publiques.
4. **Analyse de l'accès aux articles.** Afficher nombre et pourcentage sur un dénominateur explicite (articles du corpus filtré) : texte intégral gratuit vérifié, payant/restrictif vérifié, accès non déterminé. Distinguer consultation APDS et accès en ligne ; copie gratuite ≠ licence ouverte. Ne pas déduire « payant » d'un lien absent ou d'un DOI seul. Conserver URL/preuve/date de vérification ; gérer plusieurs versions et contradictions. Ajouter éventuellement une répartition tous documents séparée. Critères : totaux cohérents, catégorie inconnue visible, filtres respectés et tableau accessible accompagnant le graphique.
5. **Récits historiques de la Sangha et navigation à vapeur.** Premières pistes ci-dessous ; rechercher variantes Sangha/Sanga, Ngoko/N'Goko, Dzimou/Ndzimou, Ouesso, Bayanga, Luxembourg et Commandant-Lamy. Distinguer récit contemporain, témoignage indirect, synthèse et inventaire d'archives. Une mention de la Sangha ou un combat en aval ne suffit pas à DSPA-Core ; garder DSPA-Relevant ou indéterminé jusqu'à preuve géographique. Vérifier éditions, auteurs, pages, droits et doublons avant ajout.
6. **Veille semestrielle sans abonnement obligatoire.** Faisable comme évolution du prototype déterministe : tous les six mois, découvrir les publications depuis le dernier passage réussi, rapprocher du catalogue et produire une file de revue, puis ajouter seulement les références retenues via un parcours d'écriture distinct autorisé. Aucune activation ni insertion automatique dans Zotero ici. Les API de métadonnées ne donnent pas gratuitement les PDF payants. Conserver l'horodatage du dernier succès, borne haute figée, curseurs et décisions ; le faire avancer uniquement après succès complet. Une fenêtre de publication stricte peut manquer un article ancien indexé tardivement : garder la sélection demandée par date de publication et proposer un rattrapage séparé, explicitement signalé, des dépôts/mises à jour tardifs. [Crossref distingue publication, création et indexation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/). Tester échec/reprise, retard d'indexation, doublons, dates incomplètes et relance à résultat inchangé. Choisir ensuite l'ordonnanceur selon disponibilité et quotas, sans IA payante et sans secret dans Git.

### Premières pistes historiques vérifiées le 15 octobre

- [Chasses et voyages au Congo, chapitre XI](https://fr.wikisource.org/wiki/Chasses_et_voyages_au_Congo/11) : récit de voyage rapportant une plaque à bord du Luxembourg et des événements de 1914 sur la Sangha. Passage retrouvé dans l'index ; édition, auteur et fac-similé à vérifier avant notice. Récit rétrospectif et propos rapportés, pas journal de bord de la campagne ; contextualiser le point de vue colonial.
- [AfricaMuseum, dossier Justin Malfeyt, juillet 1914–novembre 1915](https://archives.africamuseum.be/repositories/2/archival_objects/35422) : l'inventaire décrit une lettre du 17 novembre 1914 évoquant le Luxembourg dans la Sangha. Piste archivistique institutionnelle ; texte de la lettre non consulté, numérisation/accessibilité à vérifier. Ne pas attribuer à l'inventaire le contenu d'une lettre non lue.
- [Documents parlementaires du Sénat, 1914, p. 668](https://www.senat.fr/comptes-rendus-seances/3eme/pdf/documents_parlementaires/1914/DP1914_614_726.pdf) : résultats de recherche mentionnant les études de navigation sur la Sangha jusqu'à Bayanga. Source administrative candidate pour le contexte de navigation ; contrôle du volume/page et métadonnées encore requis.

## Reprise locale — lot 20 du 15 octobre 2026

[Revue et lot limité](docs/tasks/003-review-and-apds-resumption.md) : deux rapports supplémentaires, neuf pages examinées en texte et en image ; deux pages partiellement illisibles, limites conservées. Notices existantes comparées par GET public ; propositions locales seulement. Aucun original, PDF public ou champ Zotero modifié. Pas de version complète équivalente en ligne confirmée par les deux recherches ciblées.

Compteurs actuels des registres privés : **43 scans / 565 pages examinées en OCR** (334 lisibles, 231 insuffisantes), **54 scans / 800 pages examinées visuellement** (740 lisibles, 60 partiellement illisibles). Restent **127 scans / 5 447 pages dans le suivi OCR** et **5 212 pages dans le suivi visuel**. Couverture lisible unique : 745 pages, avec 329 pages communes aux deux lectures. Les compteurs historiques ci-dessous restent inchangés ; utiliser ces compteurs récents pour la prochaine reprise.

La revue locale du socle et du prototype est consignée dans STATE ; leurs limites restent explicites. L'intégration Git est désormais autorisée après contrôles ; GitHub Pages publie depuis main. Le prochain lot APDS doit partir des statuts privés `pending`, selon le tri proportionné D005, sans réinitialisation ni import. Les deux nouveaux compléments restent soumis à validation et relecture de la notice actuelle avant application ; aucune autorisation de diffusion des scans n’en découle.

Preuves locales : `outputs/verification-revue-ocr-2026-10-15-lot20.json` et sauvegarde privée `outputs/recovery-library-review-2026-10-15/`. Le bilan narratif `outputs/bilan-revue-ocr.md` reste historique au lot 19 ; les registres JSON et leurs rapports régénérés font foi pour les compteurs du lot 20.

## Bilan historique APDS conservé

État consigné le **15 octobre 2026** ; dernier contrôle documentaire détaillé : **14 octobre 2026, lot 19**. Ce document clôt le lot de travail `feature/apds-archive-catalogue` et prépare sa reprise après l’amélioration du développement souhaitée par le responsable du projet. **L’audit exhaustif des archives n’est pas terminé.**

## Travail livré

- **118 nouvelles notices Zotero** importées en deux passes (82 puis 36), dans les collections existantes. Elles indiquent la conservation d’une copie à la Bibliothèque des APDS et leur identifiant d’inventaire. Les fichiers d’import du [catalogue](catalogue/apds-2026-10-08/README.md) sont une trace historique, pas une file à réimporter.
- Les documents pertinents ont une notice même lorsque des informations manquent ; les incertitudes restent explicites. Vingt-cinq originaux sensibles de la seconde passe sont représentés par des métadonnées minimales et un avertissement de consultation encadrée.
- **Six plans historiques expurgés, 83 pages publiques**, avec présentation, provenance et empreintes dans le [manifeste](catalogue/apds-2026-10-08/plans-publics/manifest.json). Les diagnostics, bilans et propositions historiques sont conservés avec leur attribution. La copie de Yandoumbé a été renforcée le 13 octobre ; les six copies ont été recontrôlées au fil des derniers lots.
- Affichage de la provenance, des lacunes et des avertissements de consultation dans les cartes, la liste et le tableau de la bibliothèque.
- **13 notices existantes enrichies et vérifiées après rechargement** pendant la revue OCR : quatre pour la préférence de source en ligne/provenance et neuf pour les lacunes, limites ou plans. Ce ne sont pas 13 nouveaux imports. Les autres propositions de métadonnées ne sont pas toutes appliquées.
- Les évolutions indépendantes déjà présentes sur `main` (catégories, analyses et qualité bibliographique) sont conservées lors de l’intégration.

## Couverture réelle du contrôle

Les chiffres portent sur les **fichiers scannés**, variantes comprises, et sur leurs pages PDF, pas sur un nombre de publications uniques.

| Indicateur au point d’arrêt | Réalisé | Reste / limite |
| --- | ---: | --- |
| Inventaire local | 170 PDF, 6 012 pages | L’intégralité des originaux physiques n’est pas certifiée |
| Transcriptions préparées en Markdown privé | 170 | Une conversion ne constitue pas une relecture |
| Revue OCR détaillée, page par page | 41 scans, 556 pages | 129 scans, 5 456 pages à examiner dans ce suivi |
| Lecture OCR suffisamment reconnue | 327 pages | 229 pages examinées nécessitent les images ou ont un OCR insuffisant ; certaines sont blanches |
| Contrôle visuel cumulé | 52 fichiers dont toutes les pages ont été ouvertes ; 791 pages | 5 221 pages restent à contrôler visuellement |
| Lisibilité des pages visuellement examinées | 733 pages contrôlées lisibles | 58 pages partiellement illisibles, sans certification de lecture intégrale |
| Regroupement des 41 scans relus | 36 dossiers bibliographiques | 3 guides généraux hors périmètre ; 33 dossiers concernent le catalogue |

Les contrôles OCR et visuels **se recoupent et ne doivent pas être additionnés**. Certaines variantes ont été relues sans que toutes les autres copies d’une même publication aient été comparées. Un scan ouvert n’est pas nécessairement lisible ni complet.

## Travaux ouverts du bilan initial — actualisation ci-dessus

1. **Mettre en place puis éprouver l’amélioration du développement** : périmètre désormais précisé dans les deux fiches ci-dessus ; résultats dans STATE. Conserver une procédure de validation avant publication et distinguer les changements Git des écritures dans Zotero, qui alimentent immédiatement le site public.
2. **Poursuivre la revue documentaire depuis les registres privés**, sans réinitialiser les compteurs : utiliser les restes actualisés du lot 20 ci-dessus. Revenir aux images pour les tableaux, cartes, annotations et passages mal reconnus ; conserver les limites lorsqu’un original reste illisible.
3. **Comparer les propositions restantes aux notices Zotero actuelles**, puis appliquer uniquement les compléments validés, sans écraser les enrichissements indépendants. Le lot de propositions de 36 dossiers est partiellement appliqué ; les 13 notices déjà enrichies ne signifient pas que tous leurs champs proposés ont été réconciliés. Vérifier la sauvegarde après rechargement et consigner les champs effectivement modifiés.
4. **Poursuivre la recherche des versions en ligne identiques** : vérifier titre, auteurs, date, édition/langue et pagination ; privilégier le DOI confirmé ou le dépôt institutionnel. Conserver la provenance APDS et les lacunes du scan. La référence citée dans un rapport, sa traduction ou un article ultérieur ne lui donnent pas leur DOI. Certains liens institutionnels ont été confirmés sans audit visuel du volume en ligne entier ; le lien direct vers l’édition française d’un chapitre reste à confirmer.
5. **Compléter les comparaisons de variantes et rechercher les pages manquantes**. Des scans préférables ont été identifiés, mais l’équivalence de toutes les copies et l’intégralité des originaux ne sont pas établies. Ne pas inventer les dates de rédaction à partir des périodes de terrain, ni les auteurs à partir des signataires.
6. **Préparer les autres copies publiques pertinentes**, après examen des droits et, lorsque nécessaire, expurgation ciblée. Plusieurs documents relus pourraient être diffusés ; leurs copies finales n’ont pas été produites. Les détails des retraits restent dans l’audit privé. Adapter l'examen visuel au risque selon D005 ; pour les copies expurgées, vérifier les retraits, la lisibilité, l'empreinte et l'absence de contenu retiré récupérable dans le texte, les annotations ou pièces jointes avant diffusion.
7. **Vérifier la cohérence des indicateurs de qualité avec les notices d’archives**. Le contrôle actuel de qualité reconnaît les tags d’accès `Open` et `Restricted` ; `Restricted-Original` peut encore déclencher « Accès à déterminer ». Distinguer accès à l’original et disponibilité d’une copie expurgée dans le prochain chantier, sans transformer l’avertissement en autorisation de diffusion.
8. **Suivre les anciennes versions publiques** : la révision d’une copie et la mise à jour du lien préféré dans Zotero ne retirent pas ses versions antérieures de l’historique Git ou de leurs URL immuables. Évaluer séparément le besoin de retrait de l’ancienne révision de Yandoumbé ; aucune purge d’historique ni suppression des copies distantes n’a été réalisée.

## Conditions à conserver lors de la reprise

Une notice bibliographique publique ne vaut pas autorisation de publier son PDF. La présence en ligne ne règle pas les droits de redistribution. Conserver les originaux sensibles sous consultation encadrée ; ne pas publier le corpus OCR privé, les inventaires avec chemins locaux, les constatations personnelles ou les cartes détaillées non validées. Les propositions d’un plan ancien ne prouvent pas leur mise en œuvre et ses diagnostics ne décrivent pas automatiquement la situation actuelle.

Les fichiers JSON de ce dépôt sont des **instantanés d’import d’octobre**, pas une sauvegarde exhaustive à jour du groupe Zotero. Les enrichissements ultérieurs sont tracés dans les journaux locaux. Avant tout import, comparer clés Zotero, DOI et identité bibliographique pour éviter les doublons.

## Point de reprise local — hors dépôt public

Les fichiers suivants sont conservés dans l’espace de travail local, à côté du checkout `work/dzanga-sangha-research-library`. Ils ne sont pas inclus dans le dépôt et doivent être sauvegardés séparément avant migration ou nettoyage de cet espace :

- Inventaire et contrôle final du lot 19 : `outputs/inventaire-prive-apds-final.json`, `outputs/verification-revue-ocr-2026-10-14-lot19.json`.
- Compteurs et bilan : `outputs/revue-ocr-progress.json`, `outputs/controle-visuel-progress.json`, `outputs/bilan-revue-ocr.md`.
- Décisions par page et états de reprise : `outputs/revue-ocr-prive.*`, `outputs/controle-visuel-prive.*`, `work/text-audit/`, `work/visual-audit/`, `work/review-text/`.
- Propositions et écritures Zotero : `outputs/enrichissements-notices-revue-ocr.json`, `work/zotero-online-preference-applied.json`, `work/zotero-ocr-notes-applied.json`, avec les preuves locales de vérification.

Ces dossiers privés permettent de reprendre l’analyse ; ils ne doivent pas être téléversés en bloc dans GitHub ou Zotero. La fusion clôt la branche de ce lot, pas les tâches ouvertes de cette feuille de route.
