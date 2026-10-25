# Registre récupéré — Communication, 24 octobre 2026

## Provenance et portée

Registre reconstitué à partir du fichier fourni par l'utilisateur, `PASSATION-CODEX.md`. Son empreinte et les compteurs initiaux figurent dans [provenance.json](provenance.json). Ce document rapporte une conversation antérieure : il n'est ni un export Zotero, ni un inventaire validé, ni la preuve de fichiers ou commits Perplexity existants. Les 60 identifiants DSC-001 à DSC-060 sont conservés sans renumérotation. Ils incluent familles documentaires, extraits et composantes ; ils ne représentent pas 60 œuvres indépendantes ou nouvelles.

Le périmètre de recherche inclut presse, radio, films, photographies, exposition, vulgarisation, communication institutionnelle, promotionnelle et touristique pertinente, sans condition d'indépendance journalistique. Les partenariats doivent être décrits. Le registre exploratoire peut être plus large que les catégories actuelles du hub : aucune adaptation automatique du catalogue ne découle de cette conservation.

## Fichiers et statuts séparés

- [reported-sources.tsv](reported-sources.tsv) : les **60 pistes rapportées**, toutes initialement `reported_unverified`. Chaque bloc source est conservé dans `notes_reported`, avec les sauts de ligne encodés `\n`, sa ligne d'origine et les réserves. Les titres et métadonnées de ces colonnes restent des déclarations de la passation, jamais des faits nouvellement vérifiés. `url_reported` est le premier lien rapporté, pas nécessairement une source primaire. DSC-016 et DSC-029 n'ont pas de lien individuel fourni.
- [verification-log.tsv](verification-log.tsv) : journal daté des consultations réelles et des échecs techniques, séparé de la passation. Une fiche, un synopsis, un extrait et une œuvre lue/écoutée intégralement ne constituent pas le même niveau de preuve.
- [verified-sources.tsv](verified-sources.tsv) : métadonnées confirmées par une source consultée ; une incertitude résiduelle reste explicite. Ce fichier est vide au premier commit de conservation. Les pistes non vérifiées ne sont jamais déplacées silencieusement dans ce fichier.
- [zotero-matches.tsv](zotero-matches.tsv) : rapprochements en lecture seule, distincts de la validation documentaire. Les cinq clés annoncées par la passation sont conservées dans `keys_reported`, sans être déclarées confirmées. Toutes les lignes commencent `not_checked`.

Un rapprochement à une notice Zotero ne prouve ni l'exactitude de ses métadonnées ni une vérification de l'œuvre. Une similitude de titre ne permet pas de fusionner article, épisode, traduction, rediffusion ou extrait. DSC-039 rapporte une galerie déjà liée à DSC-035 ; son identifiant est conservé comme piste de composante, sans la compter comme enquête indépendante.

## Méthode et protections

Sauvegarde documentaire d'abord, consultations ensuite. Rechercher les producteurs, éditeurs, diffuseurs et catalogues de référence ; séparer date originale, première diffusion, traduction, tournage, mise en ligne et mise à jour. Ne pas confondre la langue d'une page avec celle d'un film. Une restriction ne se déduit pas d'un simple blocage de robot. Un HTTP 200 ne prouve pas la concordance de l'œuvre. Les sons de terrain et les montages radiophoniques restent distincts.

Les corps d'articles, œuvres protégées, archives APDS, caches, clés et copies intégrales restent hors du dépôt. Aucun import Zotero, aucune fusion à main et aucun déploiement ne sont autorisés dans ce lot sans nouvel accord utilisateur. Les deux branches de recherche antérieures sont préservées ; cette récupération travaille sur sa propre branche. Les 23 médias ajoutés le 22 octobre ne doivent pas être réimportés.

## Conservation et contrôles initiaux

Comptage déterministe : 60 identifiants uniques, suite DSC-001 à DSC-060 complète, deux liens individuels manquants, cinq clés Zotero rapportées, zéro source nouvellement vérifiée au premier commit. Les blocs conservés ont été comparés caractère par caractère à ceux du fichier utilisateur après normalisation des fins de ligne. Le premier commit ne prétend pas avoir vérifié les pages citées. Les contrôles du dépôt et leur preuve liée au SHA sont consignés dans STATE et `.local/verification.json`.

La recherche historique reprendra après cette première sauvegarde, en priorité Baconnet/Écomedia, AMNH, National Geographic/Nichols et Cornell/NPR. Les nouveaux résultats devront avoir leurs propres identifiants et preuves ; redécouvrir une des 60 pistes ne constitue pas une nouveauté. Les rapports et compteurs de la suite seront ajoutés ici sans réécrire cette provenance initiale.

## Résultats de la première passe historique

Le premier commit de conservation est `292fe926c1e7eea2b972a400d5cb10a150545428`. Les paragraphes précédents décrivent ce premier état ; les fichiers de vérification sont désormais renseignés. Les 60 blocs rapportés restent inchangés et portent toujours leur statut de déclaration initiale.

Voir le [bilan historique](HISTORICAL-REVIEW.md), les [dix nouvelles pistes/entités](historical-leads.tsv) et le [bilan calculé](review-summary.json). Sur les 60 identifiants initiaux, 17 ont fait l'objet de consultations et 15 disposent de métadonnées confirmées avec limites explicites. Le fichier `verified-sources.tsv` contient 22 lignes au total, dont sept entités historiques supplémentaires ; ce n'est ni une liste de 22 œuvres nouvelles, ni une file autorisée à importer.

Le [bilan de lecture publique Zotero](zotero-snapshot-summary.json) couvre cinq pages, 459 objets dont 458 références. Cinq rapprochements annoncés sont confirmés ; 55 pistes n'ont pas de correspondance exacte selon la méthode documentée dans `zotero-matches.tsv`, ce qui ne prouve pas leur absence sous une autre version. Aucun changement du catalogue. Branche et commits locaux seulement ; aucune fusion, aucun déploiement.

## Revue déléguée du 25 octobre

La [revue et ses limites](DELEGATED-REVIEW.md) complète la première passe : [60 identifiants suivis](register-status-2026-10-25.tsv), 15 avec métadonnées confirmées directement, 25 avec métadonnées attestées selon la consultation déléguée à Perplexity, 20 encore partiels. Zéro identifiant sans première revue ; ce n'est pas une acceptation finale des 60 pistes. Les compteurs du 24 octobre ci-dessus sont conservés comme état historique.

Les résultats délégués restent séparés du fichier `verified-sources.tsv`, dont les 22 lignes initiales ne changent pas. [Quatre pages WWF/Smithsonian](delegated-verification-2026-10-25.tsv), [39 pistes restantes](delegated-sweep-2026-10-25.tsv), [cinq incertitudes historiques](perplexity-review-2026-10-25.tsv), [bilan calculé](delegated-review-summary.json). Aucun média intégralement visionné ou écouté revendiqué. Session Communication externe toujours séparée ; aucun import Zotero ou déploiement.
