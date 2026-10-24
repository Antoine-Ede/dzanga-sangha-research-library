# Premier corpus Communication — 22 octobre 2026

Clôture du 24 octobre : PR 15 fusionnée après validation utilisateur ; le correctif décrit comme « prêt à revoir » ci-dessous est intégré à main. La preuve finale de publication est conservée dans `.local/media-review/integration-2026-10-24.json`. Aucun nouvel import ; les recherches Communication suivantes passent à Perplexity sur une autre branche. Les compteurs et contrôles du bilan restent ceux du 22 octobre.

Demande : rechercher Mongabay, WWF Allemagne, National Geographic, BBC, WWF US, médias espagnols et EarthRanger. Recherche par domaines et expressions Dzanga/Dzanga-Sangha, puis inspection ciblée des pages originales : titre, signature, date, contexte local, format et accès. Pas de lecture intégrale revendiquée pour les documentaires et entretiens audio. Ce corpus de communication n'est pas une validation scientifique des affirmations des médias.

## Sélection et traçabilité

[23 notices sélectionnées](selected.json) et [registre de 48 pistes](decisions.csv). Le registre distingue sélection, alias, reprise écartée du premier lot et piste encore à vérifier. Une piste non sélectionnée n'est pas déclarée non pertinente sans examen. La recherche est un premier lot, pas une collecte exhaustive des sites ; notamment aucun résultat dans la requête ciblée National Geographic España ne prouve l'absence de contenu espagnol.

| Source / édition | Notices retenues |
| --- | ---: |
| Mongabay | 4 |
| WWF Deutschland | 3 |
| WWF US / World Wildlife | 3 |
| BBC News et BBC Mundo | 3 |
| National Geographic | 2 |
| El País (dont EFE et AFP) | 3 |
| RTVE / RNE | 2 |
| WWF España | 1 |
| EarthRanger | 1 |
| BBC One, extrait Africa | 1 |

Les contenus portent sur tourisme et activités communautaires, BaAka et pandémie, gorilles, éléphants et trafic d'ivoire, gestion et outils de suivi. La distinction repose sur le contenu éditorial : journalisme de rédaction/agence/documentaire d'une part, récits des organisations sur leurs actions d'autre part. Une dépêche EFE reprenant WWF reste une publication d'agence, mais son origine est explicitée ; elle n'est pas présentée comme un reportage de terrain indépendant. La version BBC Mundo partage l'événement de l'édition anglaise : deux notices linguistiques, une seule actualité.

## Sources et décisions délicates

- [EarthRanger, étude de cas APDS](https://www.earthranger.com/success-stories/dzanga-sangha) : titre et date du 6 mai 2025 attestés sur la page ; communication institutionnelle, pas article scientifique ni jeu de données.
- [Mongabay, reportage sur le tourisme](https://news.mongabay.com/2026/04/the-little-known-story-of-emerging-ecotourism-in-the-central-african-republic/) : signature et citation recommandée confirment David Akana. Certains noms différents des métadonnées techniques correspondent aux crédits Editor. Les éditeurs ne deviennent pas auteurs. Même vérification pour le reportage de Dzanga Bai ; quatre DOI explicitement fournis par les pages sont conservés.
- [WWF Allemagne, Limo](https://www.wwf.de/themen-projekte/bedrohte-tier-und-pflanzenarten/gorillas/limo-ein-neuer-silberruecken-in-dzanga-sangha) et deux autres pages : seule une date « Stand » est visible. Les trois dates de publication initiale restent vides, avec date de version en provenance et `STATUS:Metadata-Incomplete`.
- [El País, Luis Arranz](https://elpais.com/elpais/2017/02/24/ciencia/1487964024_824686.html) : publié le 26 février 2017, pas le 24 contenu dans l'URL. Abonnement explicite ; accès restreint conservé. Même prudence pour la dépêche sur les jumeaux gorilles. La galerie AFP est consultable, publiée le 24 juin 2020 ; les dates des photographies ne remplacent pas sa date de publication.
- [National Geographic, enquête sur l'ivoire](https://www.nationalgeographic.com/tracking-ivory/article.html) et [saisie Togo–Vietnam](https://www.nationalgeographic.com/animals/article/141107-togo-vietnam-forest-elephants-ivory-smuggling-animals-conservation) : passages explicites sur Dzanga-Sangha/Dzanga Bai ; portée régionale Relevant. Dates affichées retenues plutôt que fragments d'URL ; photographes distincts des auteurs.
- [BBC, The village of elephants](https://www.bbc.co.uk/programmes/p013vbkt) : extrait officiel daté du 16 janvier 2013 ; restriction géographique affichée, donc pas de promesse de lecture libre. Réalisateur/production non attestés : créateurs laissés vides, signalement de métadonnées incomplètes. Le clip [Forest poaching](https://www.bbc.co.uk/programmes/p006p35h) reste en attente pour l'accès.
- [RTVE, entretien sur l'ivoire](https://www.rtve.es/play/audios/24-horas-fin-de-semana/luis-arranz-trafico-marfil-deberia-estar-prohibido-desde-hace-tiempo/5371218/) et portrait de carrière : descriptions et durées officielles examinées, liens audio officiels HTTP 200 `audio/mpeg`. Pas d'écoute intégrale revendiquée. Luis Arranz est invité, pas réalisateur ; RTVE/RNE est la responsabilité éditoriale collective.

## Catalogue, droits et limites

Les 23 notices sont classées `CORPUS:Communication`, une seule nature et `SCOPE:DSPA-Relevant`. Les collections thématiques existantes restent utilisées ; aucune vingtième collection créée. Les pages institutionnelles utilisent le type webpage, les émissions leur type radio/TV. La disponibilité d'une page ou d'un audio n'est ni une licence de redistribution ni une preuve d'audience. Aucun article, image, PDF ou fichier audio n'est republié.

Index d'identité : DOI normalisé, URL avec sa requête utile conservée, titre normalisé comme garde supplémentaire. Une correspondance préexistante est conservée pour inspection ; aucune notice ancienne n'est modifiée. Créations par tableaux JSON UTF-8, contrôle des rôles autorisés par type Zotero, lecture publique immédiate et relance attendue sans création. L'interruption initiale sur le rôle TV non pris en charge est conservée dans les preuves privées ; aucun doublon ni notice vide ne doit être créé en reprise.

Le petit correctif du hub reconnaît le titre de site pour le filtre média et les responsables radio/film dans Qualité. Un invité seul ne suffit toujours pas à renseigner l'auteur/responsable ; aucune règle APDS n'est relâchée. La mise en page reste celle de la bibliothèque. Les compteurs des contenus ne constituent pas une mesure d'impact : traductions, reprises et références à une même enquête doivent être distinguées avant analyse.

Résultat exact du contrôle public dans [verification.json](verification.json) : **23/23, 458 références, 24 contenus Communication**. Relance réelle : zéro création, 23 déjà présentes. Audit public : 19 collections, seed 31/31, gouvernance et Harris valides, zéro titre vide/doublon détecté. Les 436 objets préexistants (435 références et une note) sont inchangés. Quatre nouvelles notices ont une lacune explicite : trois dates et les crédits TV.

Navigateur contrôlé avec les données publiques réelles sur le site publié et le correctif local : 24 lignes, 8 contenus institutionnels filtrés, 2 émissions RTVE et export correspondant, liens de titres officiels, mobile sans débordement de page, aucune erreur JavaScript. Dénominateur recherche 434. Le site publié affiche encore 128 alertes ; le correctif prêt à revoir ramène ce chiffre à 126 en reconnaissant correctement les responsabilités et diffuseurs des deux émissions radio. Les quatre lacunes réelles restent signalées. Ce correctif n'est pas encore publié.

Les sources brutes, instantanés avant/après, journal de clés et scripts authentifiés sont privés dans `.local/media-review/`, exclus du dépôt. Pour annuler un ajout, inspecter sa version actuelle et sauvegarder son JSON avant toute suppression individuelle ; ne pas rétablir un instantané global du groupe.
