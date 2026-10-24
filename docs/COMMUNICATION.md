# Médias et communication

L'onglet Communication recense les contenus médiatiques présents dans Zotero : presse, magazines, films/documentaires, reportages vidéo ou TV, radio et podcasts. Le catalogue reste la source de vérité ; une notice ajoutée dans le groupe apparaît au prochain chargement. Il ne s'agit ni d'une veille activée ni d'un import automatique depuis les médias.

## Entrée dans la rubrique

Les types Zotero `newspaperArticle`, `magazineArticle`, `film`, `videoRecording`, `tvBroadcast`, `radioBroadcast` et `podcast` apparaissent automatiquement. Ce choix suppose que leur pertinence Dzanga-Sangha a été vérifiée avant ajout à la bibliothèque.

Pour une page web, une interview ou un type ambigu, ajouter `CORPUS:Communication` après vérification. Une page de protocole, une donnée audiovisuelle de recherche ou une interview de terrain n'est pas classée communication simplement parce qu'elle est disponible en ligne. Aucun titre n'est analysé automatiquement pour lui attribuer cette rubrique.

Renseigner titre, auteur/réalisateur, date de publication/diffusion, média/studio/diffuseur, langue et URL originale. Conserver les sites et sujets dans les tags existants. L'ajout à la rubrique ne confère pas DSPA-Core, ne certifie pas les affirmations du contenu et ne donne pas un droit de redistribution.

## Journalisme et communication institutionnelle

Le responsable confirme le 22 octobre que les deux doivent être inclus et distingués :

- `COMMUNICATION:Journalistic` : couverture journalistique éditoriale identifiée ;
- `COMMUNICATION:Institutional` : contenu de communication d'une organisation ou d'un projet identifié.

Absence des deux tags ou présence contradictoire : « À préciser ». Ne pas déduire la nature du seul nom de l'organisme ou du format. Un documentaire commandité et un reportage de rédaction peuvent partager le même format.

## Consultation et indicateurs

Accès direct : `?section=communication`. Filtres propres : texte, format, année, média/diffuseur et nature. Les filtres sont conservés dans l'URL avec des paramètres `media_*` ; ils ne changent pas ceux de la bibliothèque. L'export CSV porte uniquement sur la sélection communication et indique le lien du document et le lien Zotero.

Le titre suit la règle du hub : PDF public disponible, sinon URL du document, puis DOI en recours ; lien Zotero distinct. Pas de lecture de fichiers privés Windows ni de publication d'originaux par cet onglet.

Les chiffres décrivent la sélection et son dénominateur : nombre de contenus, nombre de médias/diffuseurs renseignés, période des contenus datés et nombre sans année. Un contenu repris sur plusieurs sites doit être examiné avant de compter des reprises comme des productions originales. Aucune audience, vue ou influence n'est inventée. L'impact de communication demande des preuves supplémentaires datées, avec source et méthode.

Les médias restent consultables dans la bibliothèque générale et forment une catégorie distincte. Ils sont exclus des indicateurs de l'onglet Analyse de la recherche, dont le dénominateur le précise. Les alertes de qualité bibliographique restent visibles et ne sont pas effacées par ce classement.

## Limites du premier lot

Le [lot de recherche du 22 octobre](../reviews/media-2026-10-22/README.md) ajoute ensuite 23 notices vérifiées ; le groupe comprend maintenant 458 références et 24 contenus Communication. Les chiffres du paragraphe suivant décrivent la livraison initiale de l'interface, avant ces ajouts. Dates manquantes et crédits non attestés restent signalés ; une fiche publique n'implique pas la lecture libre de son média. Les émissions radio et TV conservent les rôles Zotero propres à leur type, sans transformer un invité ou un diffuseur en réalisateur.

Le 22 octobre, une notice existante de type magazine est éligible dans l'instantané public de 435 références ; sa nature reste à préciser. Aucun nouveau média n'a été importé ou recherché exhaustivement et aucun tag Zotero n'a été modifié. Les exemples des tests sont fictifs et ne sont pas livrés comme références du catalogue.

Le lot dépend du correctif des titres de la PR 13. L'utilisateur a validé l'aperçu et autorisé la fusion des deux PR le 22 octobre sous condition de conserver le style et les fonctions existants. Preuve de livraison exacte dans `.local/communication-preview/integration.json` ; les travaux APDS restent dans l'autre session.
