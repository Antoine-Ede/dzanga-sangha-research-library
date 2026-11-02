# Paquet de vérification Perplexity — 64 entrées SUP

Ce paquet fournit les 64 entrées à vérifier du supplément Communication Dzanga-Sangha.
Il a été extrait localement du registre de conservation le 2 novembre 2026.
Tous les éléments ci-dessous sont des déclarations rapportées, non des métadonnées déjà vérifiées.
Les URL servent de pistes : une URL rapportée ne prouve ni son accessibilité actuelle, ni les champs bibliographiques associés.

## Consignes de sécurité documentaire

- Vérifier uniquement les 64 blocs ci-dessous, avec des sources réellement consultées.
- Ne pas inventer date, auteur, langue, durée, pagination, droits ou relation entre versions.
- Un rapprochement indiqué plus bas est seulement un candidat ; aucune fusion ni déduplication automatique.
- Ne pas proposer d'import Zotero, de modification Git ou de publication.
- Si une source est inaccessible, conserver `blocked` ou `partial` plutôt que compléter par inférence.

## Format de retour requis

Produire un TSV, une ligne par identifiant, avec les colonnes exactes suivantes :

```text
id	status	title_confirmed	creator_confirmed	date_confirmed	type_confirmed	source_url	evidence_summary	dzanga_relevance	relationship_or_duplicate	limitations	checked_at
```

Les seuls statuts admis sont `verified_delegated`, `partial`, `blocked` et `duplicate_candidate`.
Un résultat incomplet doit rester une ligne avec ses limites explicites. Si l'interface ne permet pas de produire des fichiers, renvoyer le TSV complet dans un bloc de code, puis un README Markdown séparé ; ne pas prétendre qu'un téléchargement a été créé.

## Six entrées déjà traitées — à exclure

- SUP-04 : partiel ; date d'en-tête non validée.
- SUP-27 : bloqué ; page et sommaire WWF non récupérés.
- SUP-51 : métadonnées déléguées confirmées (Los Angeles Times, 1994).
- SUP-57 : partiel ; versions EN/FR consultées, année éditoriale non confirmée.
- SUP-64 : partiel ; référence secondaire Chadwick, original National Geographic non retrouvé.
- SUP-65 : partiel ; CARPO/WWF confirmé en partie, fin de l'entretien et identité complète non établies.

## Rapprochements locaux seulement (ne sont pas des identités démontrées)

| SUP | Candidat local | Relation rapportée | Limite |
| --- | --- | --- | --- |
| SUP-05 | MEDIA22:elpais-twins | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-05 | DEC22:39 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-26 | DEC22:33 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-28 | MEDIA22:wwfus-inside | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-28 | DEC22:31 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-33 | DSC-040 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-33 | DSC-041 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-33 | DSC-040 | enrichment_reported_by_handoff | May be a companion, print/web version or relay; do not merge automatically. |
| SUP-34 | DEC22:36 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-41 | HIS-001 | same_underlying_book_candidate_edition_pending | Louis Sarno book, not film SUP-01 or Bayaka DSC-050; specific edition not confirmed. |
| SUP-41 | HIS-010 | same_underlying_book_candidate_edition_pending | Louis Sarno book, not film SUP-01 or Bayaka DSC-050; specific edition not confirmed. |
| SUP-61 | MEDIA22:mongabay-kienast | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-61 | DEC22:02 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-62 | MEDIA22:mongabay-elephants | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-62 | DEC22:04 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-66 | DSC-055 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-66 | DSC-055 | enrichment_reported_by_handoff | May be a companion, print/web version or relay; do not merge automatically. |
| SUP-68 | DSC-043 | exact_reported_url_overlap | Same link or title does not identify every work in a family or turn an index/citation into the target work. |
| SUP-68 | DSC-043 | enrichment_reported_by_handoff | May be a companion, print/web version or relay; do not merge automatically. |

## Blocs sources exacts à examiner

### SUP-01 — Song from the Forest — film

- Date(s) rapportée(s) : 2013; sorties 2014–2015.
- Responsabilité / langue rapportée : Michael Obert; Tondowski Films; Heino Deckert; image Siri Klug; montage Wiebke Grundler.
- Liens :
  - http://songfromtheforest.com/
  - http://songfromtheforest.com/files/sf_poster_a4.pdf
- État, relation et suite : Site et affiche repérés. Première mondiale annoncée le 21 novembre 2013, IDFA. Ne pas confondre avec le livre de Sarno. Durée, langues, droits et accès à confirmer.

### SUP-02 — Inside the World of Louis Sarno, the Pygmy Chief From New Jersey

- Date(s) rapportée(s) : 2015.
- Responsabilité / langue rapportée : Newsweek.
- Liens :
  - https://www.newsweek.com/2015/04/24/inside-world-louis-sarno-pygmy-chief-new-jersey-322714.html
- État, relation et suite : Reportage situant Sarno à Yandoumbé/Bayanga; contexte du film. Date exacte, auteur et crédits à relever; ne pas déduire la date de l’URL.

### SUP-03 — The Man Who Spent 30 Years in the Rainforest Preserving the Music of the Bayaka

- Date(s) rapportée(s) : 20 juillet 2016 rapporté.
- Responsabilité / langue rapportée : VICE.
- Liens :
  - https://www.vice.com/en/article/louis-sarno-spent-30-years-in-the-rainforest-preserving-the-music-of-the-bayaka/
- État, relation et suite : Musique, habitants, conservation; signature et métadonnées à vérifier.

### SUP-05 — El nacimiento de unos gemelos de gorila, una pequeña…

- Date(s) rapportée(s) : 10 février 2016 rapporté.
- Responsabilité / langue rapportée : El País; espagnol.
- Liens :
  - https://elpais.com/elpais/2016/02/10/ciencia/1455118661_969240.html
- État, relation et suite : Titre incomplet à compléter. Malui, Makumba, Bai Hokou; WWF et David Greer cités. Retrouver communiqué/images originaux, signature et crédits.

### SUP-06 — Pom, The Red Elephant

- Date(s) rapportée(s) : 19 août 2015.
- Responsabilité / langue rapportée : Andrea K. Turkalo; WCS Wild View.
- Liens :
  - https://blog.wcs.org/photo/2015/08/19/red-elephant-andrea-turkalo-africa/
- État, relation et suite : Publication photographique explicitement à Dzanga Bai. Crédits et droits à relever.

### SUP-07 — Missing For 9 Years, Ahmed The Elephant Returns

- Date(s) rapportée(s) : 6 avril 2016.
- Responsabilité / langue rapportée : Vicki Croke; WBUR.
- Liens :
  - http://archives.wbur.org/thewildlife/2016/04/06/missing-for-9-years-ahmed-the-elephant-returns/
- État, relation et suite : Texte consulté; article illustré, pas podcast établi. Photos Turkalo/WCS et Elizabeth Bennett/WCS. Signale film WCS sur le retour de Turkalo en 2014: rapprocher S17.

### SUP-08 — Oka! — film et bande originale

- Date(s) rapportée(s) : Tournage 2009 rapporté; sortie à vérifier.
- Responsabilité / langue rapportée : Lavinia Currier.
- Liens :
  - http://archive.rockpaperscissors.biz/index.cfm/fuseaction/current.bio/project_id/605.cfm
- État, relation et suite : Source promotionnelle situant tournage à Dzanga-Sangha. Fiction inspirée de Sarno, PAS documentaire. Retrouver producteur/distributeur primaire et année.

### SUP-09 — A Space in the Heart of Africa

- Date(s) rapportée(s) : Inconnue.
- Responsabilité / langue rapportée : Repérage Mammal Watching.
- Liens :
  - https://www.mammalwatching.com/gd_place/central-african-republic/
  - https://www.mammalwatching.com/gd_place/democratic-republic-of-congo/
- État, relation et suite : Environ 50 minutes rapportées; partiellement Dzanga-Sangha et Epulu en RDC. Auteur, année, production et diffusion autorisée inconnus.

### SUP-10 — A Kingdom for the Dzanga Gorillas

- Date(s) rapportée(s) : 2006/2007/2017 selon catalogues; Blu-ray 2009.
- Responsabilité / langue rapportée : Emmanuel Robin annoncé réalisateur par édition commerciale; Discovery Animal Planet mentionné.
- Liens :
  - https://tv.apple.com/us/movie/a-kingdom-for-the-dzanga-gorillas/umc.cmc.1wagp80809wicntdgn2bl04j3
  - https://www.primevideo.com/detail/0OSEVI26YWOQBE4NYEGQL9MZCB?tr=nl
  - https://www.amazon.com/-/es/Kingdom-Dzanga-Gorillas-Narrated/dp/B0027VD3P4
  - https://www.roku.com/whats-on/tv-shows/a-kingdom-for-the-dzanga-gorillas?id=9e695d5af8c45de080bcd9ec54b50e61
  - https://www.wga.org/uploadedfiles/foreign_levies/a_d_titles.pdf
- État, relation et suite : Chloé Cipolletta et habituation. Apple: 2006/75 min; Prime: 2017/52 min et Film Ideas dans champ réalisateur; Blu-ray sortie 11 août 2009/50 min/Razor; Roku 2007/60 min. WGA mentionne 2006. Une famille provisoire, ne pas multiplier films ni attribuer réalisation à une société sans preuve.

### SUP-11 — Abenteuer Urwald — Unter Gorillas

- Date(s) rapportée(s) : Production Allemagne 2010; rediffusion 29 octobre 2019.
- Responsabilité / langue rapportée : Stefanie Zeyn et Thomas Behrend sur fiche BR.
- Liens :
  - https://www.br.de/fernsehen/ard-alpha/programmkalender/sendung-2517572.html
  - https://www.crew-united.com/de/Expeditionen-ins-Tierreich-Abenteuer-Urwald-Unter-Gorillas__141741.html
- État, relation et suite : Fiche diffuseur: Bai Hokou, Makumba, Angelique Todd; making-of. Créneau 20h15–21h ne prouve pas durée exacte. Relever rôles complets.

### SUP-12 — Primeval Forest Adventure — Among Gorillas / À la découverte des gorilles des forêts vierges

- Date(s) rapportée(s) : Apple 2016/44 min; guide français 2010.
- Responsabilité / langue rapportée : Thomas Behrend; Stefanie Zeyn annoncée réalisatrice par guide français.
- Liens :
  - https://tv.apple.com/gb/movie/primeval-forest-adventure-among-gorillas/umc.cmc.16kampanw4qxvj2lbmlqznom4
  - https://www.telestar.fr/programme-tv/fiche/152842994/a-la-decouverte-des-gorilles-des-forets-vierges
- État, relation et suite : Titres internationaux probablement liés à S11; identité de montage à prouver, dates d’édition distinctes de production.

### SUP-13 — Gorillas — Kings of the Jungle / Gorillas: The Gentle Giants

- Date(s) rapportée(s) : 2018/45 min; autre titre annoncé 2020.
- Responsabilité / langue rapportée : Thomas Behrend.
- Liens :
  - https://iwonder.com/titles/gorillas-kings-of-the-jungle-9abdc8ca6a774e649257613bc94fe1f0
- État, relation et suite : Makumba/Dzanga-Sangha; catalogue signale autre programme 2020 au synopsis voisin. Une piste familiale: comparer génériques avec S11–S12. Aucun lien individuel du titre 2020 conservé.

### SUP-14 — From Jersey to the Jungle

- Date(s) rapportée(s) : Indexation 20 janvier 2016; récit situant voyage janvier 2016.
- Responsabilité / langue rapportée : Susan Schulman; Delayed Gratification.
- Liens :
  - https://www.slow-journalism.com/from-the-archive/from-jersey-to-the-jungle
- État, relation et suite : Récit Sarno et sons crédités Schulman. Date, numéro original et republication à stabiliser; sons comme composantes sauf publication autonome prouvée.

### SUP-15 — Iris n° 27 — photographie à Dzanga-Sangha

- Date(s) rapportée(s) : 2020; dépôt URL novembre 2021.
- Responsabilité / langue rapportée : AEFONA; espagnol.
- Liens :
  - https://www.aefona.org/wp-content/uploads/2021/11/iris-27-2020.pdf
- État, relation et suite : PDF repéré par indexation; auteur, titre contribution, page et légende à retrouver. Ne pas confondre dépôt et numéro.

### SUP-16 — Index d’auteur Andrea K. Turkalo

- Date(s) rapportée(s) : Page évolutive.
- Responsabilité / langue rapportée : WCS Wild View.
- Liens :
  - https://blog.wcs.org/photo/author/aturkalo/
- État, relation et suite : Outil de dépouillement, PAS œuvre supplémentaire par défaut. Biographie: début 1990, départ avril 2013, retour octobre 2014 rapportés.

### SUP-17 — Return to Dzanga

- Date(s) rapportée(s) : Page 17 mars 2016; retour terrain automne/octobre 2014.
- Responsabilité / langue rapportée : WCS; générique non relevé.
- Liens :
  - https://www.wcs.org/wildcards/posts/return-to-dzanga
  - https://cdn.wcs.org/2016/03/18/6sdq21m3c0_WCS_AnnualReport15.pdf
- État, relation et suite : Page WCS consultée: court film, départ 2013. Rapport annuel 2015 pages imprimées 24–25: Andrea Turkalo and the Return to Dzanga Bai, retour automne 2014. Film et rapport distincts; date page ≠ première diffusion. Durée/crédits à relever; lien possible S07.

### SUP-18 — Researcher Studying Endangered Elephants Flees CAR

- Date(s) rapportée(s) : 12 juin 2013 rapporté.
- Responsabilité / langue rapportée : WCS Newsroom.
- Liens :
  - https://newsroom.wcs.org/News-Releases/articleType/ArticleView/articleId/5597/Researcher-Studying-Endangered-Elephants-Flees-CAR.aspx
- État, relation et suite : Communication contemporaine du départ de Turkalo.

### SUP-19 — Statement on Violence in Central African Republic

- Date(s) rapportée(s) : À relever.
- Responsabilité / langue rapportée : WCS.
- Liens :
  - https://newsroom.wcs.org/News-Releases/articleType/ArticleView/articleId/6520/Statement-on-Violence-in-Central-African-Republic.aspx
- État, relation et suite : Déclaration comprenant citation de Turkalo sur Dzanga Bai; ne pas dater par les seuls événements.

### SUP-20 — STUDY: A Lost Century for Forest Elephants / A Lost Century

- Date(s) rapportée(s) : Communiqué 30 août 2016; indexation Wildcards 2022 à clarifier.
- Responsabilité / langue rapportée : WCS.
- Liens :
  - https://newsroom.wcs.org/News-Releases/articleType/ArticleView/articleId/9235/STUDY-A-Lost-Century-for-Forest-Elephants.aspx
  - https://www.wcs.org/wildcards/posts/a-lost-century
- État, relation et suite : Communication d’étude démographique Dzanga Bai; comparer reprise Wildcards au communiqué; relier article scientifique sans dupliquer corpus recherche.

### SUP-21 — Elephant Ingenuity

- Date(s) rapportée(s) : 3 novembre 2014 rapporté.
- Responsabilité / langue rapportée : WCS Wild View; Andrea Turkalo associée.
- Liens :
  - https://blog.wcs.org/photo/2014/11/03/elephant-ingenuity/
- État, relation et suite : Photo; légende/localisation à vérifier, nom de Turkalo insuffisant seul.

### SUP-22 — Elephant Path / Njaia Njoku

- Date(s) rapportée(s) : 2018; versions 79 et 52 minutes.
- Responsabilité / langue rapportée : Todd McGrain; production McGrain, Scott Anger, Natalie Ruiz Tofano; image Anger; montage McGrain/Sara Khaki; musique Alexander Balanescu selon festival.
- Liens :
  - https://www.toddmcgrain.com/work/documentary-film
  - https://www.docnyc.net/film/elephant-path/
  - https://www.newday.com/films/elephant-path-njaia-njoku
  - https://catapultfilmfund.org/films/ElephantPathNjaiaNjoku/
  - https://eatdrinkfilms.com/2018/06/07/listen-to-the-elephant-path/
- État, relation et suite : Turkalo, Sessely Bernard, Zephirine Mbele, Dzanga Bai. DOC NYC 79 min/US 2018/langues English Sangho Bayaka; New Day 52 min/sous-titrage annoncé. Première mondiale SF DocFest juin 2018; DOC NYC première new-yorkaise. Vérifier versions, rôles et langues, pas deux films par défaut.

### SUP-23 — The Elephant Watcher / Elephant Watch

- Date(s) rapportée(s) : Web 4 mai 2015; numéro 11 mai.
- Responsabilité / langue rapportée : Peter Canby; photo Luca Zanetti; The New Yorker.
- Liens :
  - https://www.newyorker.com/magazine/2015/05/11/elephant-watch
- État, relation et suite : Turkalo et Dzanga Bai; titre et dates édition/web à distinguer.

### SUP-24 — The Forest Elephants — vidéo

- Date(s) rapportée(s) : 2015; date et durée à relever.
- Responsabilité / langue rapportée : The New Yorker.
- Liens :
  - https://www.newyorker.com/video/watch/notes-from-all-over-the-forest-elephants
- État, relation et suite : Vidéo distincte à relier S23; générique et lecture à vérifier.

### SUP-25 — The Forest Elephants of the Central African Republic Are in Peril

- Date(s) rapportée(s) : 14 novembre 2018.
- Responsabilité / langue rapportée : Peter Canby; The New Yorker.
- Liens :
  - https://www.newyorker.com/culture/culture-desk/the-forest-elephants-of-the-central-african-republic-are-in-peril
- État, relation et suite : Article autour du film Elephant Path; publication distincte du film.

### SUP-26 — Good conservation means human opportunity and human rights

- Date(s) rapportée(s) : 24 mars 2020 rapporté.
- Responsabilité / langue rapportée : WWF US.
- Liens :
  - https://www.worldwildlife.org/news/stories/good-conservation-means-human-opportunity-and-human-rights/
- État, relation et suite : Droits humains et opportunités locales; titre affiché peut varier: Justice and Conservation Unite in Dzanga-Sangha. Relever canonique.

### SUP-28 — Inside the Congo Basin’s Dzanga-Sangha Protected Area

- Date(s) rapportée(s) : 19 novembre 2025 rapporté.
- Responsabilité / langue rapportée : WWF US.
- Liens :
  - https://www.worldwildlife.org/news/stories/inside-the-congo-basins-dzanga-sangha-protected-area/
- État, relation et suite : Page consacrée au site; titre indexé également Wildlife & Community United. Relever titre affiché exact.

### SUP-29 — Conservation Insiders Series — segment Dzanga-Sangha

- Date(s) rapportée(s) : À établir.
- Responsabilité / langue rapportée : WWF US.
- Liens :
  - https://www.worldwildlife.org/support/philanthropy/partners-in-conservation/conservation-insiders-series/
- État, relation et suite : Index de webinaires: isoler épisode, intervenants, date et lecteur. Pas encore une œuvre individualisée.

### SUP-30 — Dzanga-Sangha Day 2025

- Date(s) rapportée(s) : Événement 18–20 novembre 2025; page décembre 2025 date divergente.
- Responsabilité / langue rapportée : HIOH; gouvernement RCA; WWF.
- Liens :
  - https://www.helmholtz-hioh.de/en/newsroom/news/detail/news/dzanga-sangha-day-2025/
- État, relation et suite : Bangui et Bayanga; date page 1/15 décembre rencontrée à clarifier. Rechercher vidéo récapitulative sans inventer URL.

### SUP-31 — HIOH launches the INFORBIO research project on forest management and zoonoses surveillance

- Date(s) rapportée(s) : Page indexée 27 juillet 2026; lancement octobre 2024; mission octobre 2025.
- Responsabilité / langue rapportée : HIOH.
- Liens :
  - https://www.helmholtz-hioh.de/en/newsroom/news/detail/news/hioh-launches-the-inforbio-research-project-on-forest-management-and-zoonoses-surveillance/
- État, relation et suite : Mission six semaines; Dzanga-Sangha, Lobéké, Campo Ma’an. Multisite; dates événement/page distinctes.

### SUP-32 — HIOH Research Worldwide / About HIOH

- Date(s) rapportée(s) : Pages évolutives.
- Responsabilité / langue rapportée : HIOH.
- Liens :
  - https://www.helmholtz-hioh.de/en/research/hioh-research-worldwide/
  - https://www.helmholtz-hioh.de/en/about-us/
- État, relation et suite : Contexte partenariats WWF/Institut Pasteur de Bangui et laboratoire satellite. Pages institutionnelles, pas annonces historiques datées arbitrairement.

### SUP-33 — Report in GEO magazine: Virus hunt in tropical rainforests

- Date(s) rapportée(s) : Article GEO août 2024; terrain février 2024; relais HIOH 2026.
- Responsabilité / langue rapportée : Jörn auf dem Kampe; Adrienne Surprenant et Martin Pauer.
- Liens :
  - https://www.helmholtz-hioh.de/en/newsroom/news/detail/news/report-in-geo-magazine-virus-hunt-in-tropical-rainforests/
- État, relation et suite : DÉJÀ PREMIÈRE PASSATION DSC-040: enrichissement, pas nouvelle œuvre. Relier article, mission et relais sans fusionner.

### SUP-34 — The first rule of gorilla tracking? Listen well / El primer consejo para rastrear gorilas: escuchar con atención

- Date(s) rapportée(s) : Anglais 5 mai 2020; espagnol 13 mai 2020.
- Responsabilité / langue rapportée : Andy Isaacson; WWF US.
- Liens :
  - https://www.worldwildlife.org/news/stories/the-first-rule-of-gorilla-tracking-listen-well/
  - https://www.worldwildlife.org/descubre-wwf/historias/el-primer-consejo-para-rastrear-gorilas-escuchar-con-atencion
- État, relation et suite : Ossolo Dacko et pisteurs BaAka. Deux versions à comparer, dates propres et crédits photo distincts. Une famille provisoire.

### SUP-35 — Protecting the Sangha Tri-National

- Date(s) rapportée(s) : À relever.
- Responsabilité / langue rapportée : WWF US / GEF.
- Liens :
  - https://www.worldwildlife.org/our-work/funds/wwf-gef/projects/strengthening-transboundary-conserved-area-management-of-the-sangha-tri-national-tns/
- État, relation et suite : Fiche de projet multisite; ne pas attribuer toutes activités à Dzanga-Sangha.

### SUP-36 — Trip to Central African Republic, Feb 5–18th 2024

- Date(s) rapportée(s) : Mission février 2024; indexation page février 2025 à confirmer.
- Responsabilité / langue rapportée : HIOH/HZI.
- Liens :
  - https://www.helmholtz-hioh.de/en/newsroom/news/detail/news/hioh-hzi-reise-in-die-zentralafrikanische-republik-5-18-februar-2024/
- État, relation et suite : Récit Bayanga, Dzanga Bai, WWF, BaAka, suivi sanitaire gorilles; équipe GEO présente. Publication distincte de GEO/relais.

### SUP-37 — One Health Exploratories gain momentum

- Date(s) rapportée(s) : Page indexée 9 septembre 2026.
- Responsabilité / langue rapportée : HIOH.
- Liens :
  - https://www.helmholtz-hioh.de/en/newsroom/news/detail/news/one-health-exploratories-gain-momentum/
- État, relation et suite : Corps du contenu: postes de santé villageois autour APDS, prélèvements, contacts animaux/environnement. Date et crédits à confirmer.

### SUP-38 — Andrea’s Story — newsletter

- Date(s) rapportée(s) : Août 2017 selon index.
- Responsabilité / langue rapportée : Elephant Listening Project.
- Liens :
  - https://www.elephantlisteningproject.org/about-elp/newsletters/
- État, relation et suite : Isoler document et titre complet depuis index; ne pas considérer bulletin individuel déjà récupéré.

### SUP-39 — Exclusive Video — Etta (#2)

- Date(s) rapportée(s) : Date originale inconnue; indexation 2014 non probante.
- Responsabilité / langue rapportée : Elephant Listening Project; vidéos Andrea Turkalo.
- Liens :
  - https://www.elephantlisteningproject.org/1316e2/
- État, relation et suite : Etta/Etta II/Ettie à Dzanga Bai. Page destinée aux adoptants; caractère exclusif explicite. Indexation publique ≠ droit diffusion; accès et date à clarifier.

### SUP-40 — Where Are You? — acoustic arrays

- Date(s) rapportée(s) : À établir.
- Responsabilité / langue rapportée : Elephant Listening Project.
- Liens :
  - https://www.elephantlisteningproject.org/acoustic-arrays/
- État, relation et suite : Vulgarisation réseaux microphones et observations Dzanga Bai; date/auteur/médias à compléter.

### SUP-41 — Song from the Forest — livre de Louis Sarno

- Date(s) rapportée(s) : 1993; éditions ultérieures distinctes.
- Responsabilité / langue rapportée : Louis Sarno; Houghton Mifflin annoncé pour édition US.
- Liens :
  - https://archive.org/details/songfromforestmy00sarn_1
  - https://www.jstor.org/stable/852594
- État, relation et suite : Notice 1993 corroborée par recension. ISBN, sous-titre exact, édition et lieux à relever. Distinct du film S01 et Bayaka 1995 DSC-050.

### SUP-42 — Victims of War: the Jungle Gorillas, and Tourism

- Date(s) rapportée(s) : 31 mars 1999, A3 selon bibliographie.
- Responsabilité / langue rapportée : Ian Fisher; The New York Times.
- Liens :
  - https://pdf.wri.org/eaa_wp6.pdf
- État, relation et suite : Uniquement référence secondaire WRI; original et part exacte Dzanga-Sangha à retrouver. Aucun lien NYT inventé.

### SUP-43 — D-20 Dzanga, Nov 28 1996

- Date(s) rapportée(s) : 28 novembre 1996 date d’objet.
- Responsabilité / langue rapportée : Archives AMNH.
- Liens :
  - https://data.library.amnh.org/archives/repositories/3/archival_objects/25185
- État, relation et suite : Notice d’objet; nature/support et diffusion publique inconnus. Date objet ≠ publication; ne pas annoncer documentaire.

### SUP-44 — How Humans Benefit From a Highway of Trails Created by African Forest Elephants

- Date(s) rapportée(s) : 9 octobre 2020.
- Responsabilité / langue rapportée : Smithsonian Magazine.
- Liens :
  - https://www.smithsonianmag.com/science-nature/how-humans-benefit-highway-trails-created-african-forest-elephants-180976045/
- État, relation et suite : Sentiers éléphants/usages humains/zonage Dzanga-Sangha. Auteur, photos et étude source à relever.

### SUP-45 — Central Africa’s secretive forest elephants

- Date(s) rapportée(s) : 26 août 1999.
- Responsabilité / langue rapportée : CNN.
- Liens :
  - https://www.cnn.com/NATURE/9908/26/africa.elephants/
- État, relation et suite : Titre/date/dateline Dzanga-Ndoki repérés; extraction intégrale échouée. Signature, vidéo éventuelle et durée non établies.

### SUP-46 — Africa: Forests under Threat — recueil

- Date(s) rapportée(s) : Novembre 2002 selon texte; URL dépôt 2013.
- Responsabilité / langue rapportée : World Rainforest Movement; coordination Ricardo Carrere; édition Hersilia Fonseca.
- Liens :
  - https://wrm.org.uy/wp-content/uploads/2013/04/Africa_Forests_under_Threat.pdf
- État, relation et suite : PDF consulté; recueil de bulletins, éditions FR/ES annoncées. Distinguer recueil et articles originaux; accusations attribuées au WRM.

### SUP-47 — Communication WRM mentionnant tournage CNN Wild Planet

- Date(s) rapportée(s) : Septembre 1998 dans recueil.
- Responsabilité / langue rapportée : WRM; Gary Strieker et Giuseppe Vassallo/WEESA mentionnés.
- Liens :
  - https://wrm.org.uy/wp-content/uploads/2013/04/Africa_Forests_under_Threat.pdf
- État, relation et suite : Texte sur exploitation forestière en zone conservation; allégations attribuées. Épisode CNN original sans titre/lien établi. Relation S45 inconnue.

### SUP-48 — Logging companies destroy “Pygmies’” livelihoods / Las compañías madereras destruyen las formas de sustento de los “Pigmeos”

- Date(s) rapportée(s) : Bulletin 59, juin 2002.
- Responsabilité / langue rapportée : WRM; anglais/espagnol.
- Liens :
  - https://www.wrm.org.uy/bulletins/issue-59
  - https://www.wrm.org.uy/africa/central-african-republic?field_site_section_term_target_id=All&field_subjects_target_id=All&page=1
  - https://www.wrm.org.uy/es/africa/republica-centroafricana?field_site_section_term_target_id=All&field_subjects_target_id=All&page=1
- État, relation et suite : Bulletin/index retrouvés; liens individuels à isoler. Comparer avec BBC S55, reprise possible non démontrée; dates migration ≠ bulletin.

### SUP-49 — Stop the Carnage

- Date(s) rapportée(s) : Date originale incertaine; indexation novembre 2013 à ne pas entériner.
- Responsabilité / langue rapportée : Smithsonian Magazine; signature à relever.
- Liens :
  - https://www.smithsonianmag.com/science-nature/stop-the-carnage-105626888/
- État, relation et suite : Texte consulté: Greer, Cipolletta, Bayanga, Bai Hokou, Makumba, Dzanga Bai. Retrouver numéro/date et auteur dans en-tête complet.

### SUP-50 — Study sheds light on unique social character of forest elephants

- Date(s) rapportée(s) : Piste février 2021; étude décembre 2020.
- Responsabilité / langue rapportée : ScienceDaily; institution originale à retrouver.
- Liens :
  - https://www.sciencedaily.com/releases/2021/02/210223121646.htm
- État, relation et suite : Observations Dzanga Bai 1995–2010; communication ≠ article Animal Behaviour. Date observation ≠ publication.

### SUP-52 — New Jersey Native Is a Pygmy in Heart, Spirit

- Date(s) rapportée(s) : 25 février 2000.
- Responsabilité / langue rapportée : Ann M. Simmons; Los Angeles Times.
- Liens :
  - https://www.latimes.com/archives/la-xpm-2000-feb-25-mn-2463-story.html
- État, relation et suite : Texte consulté: Sarno, lieu Batali, Turkalo/Dzanga-Ndoki; ne pas remplacer Batali par Yandoumbé. Titres historiques conservés sans adopter vocabulaire.

### SUP-53 — Giving the Forest Back to Pygmies

- Date(s) rapportée(s) : 25 février 2000.
- Responsabilité / langue rapportée : Los Angeles Times; signature non confirmée.
- Liens :
  - https://www.latimes.com/archives/la-xpm-2000-feb-25-mn-2448-story.html
- État, relation et suite : Page repérée, extraction échouée; accès forêt/BaAka/Dzanga-Ndoki. Possible dossier commun S52, pas même article.

### SUP-54 — Grand March of an American Misfit

- Date(s) rapportée(s) : 20 janvier 2002.
- Responsabilité / langue rapportée : Los Angeles Times; signature à relever.
- Liens :
  - https://www.latimes.com/archives/la-xpm-2002-jan-20-tm-23784-story.html
- État, relation et suite : Portrait Mike Fay, Dzanga-Sangha/Nouabalé-Ndoki et John Robinson WCS. Portée régionale, métadonnées complètes à relever.

### SUP-55 — Logging threatens Pygmies’ forest life

- Date(s) rapportée(s) : 4 juin 2002.
- Responsabilité / langue rapportée : BBC News.
- Liens :
  - http://news.bbc.co.uk/2/hi/africa/2023663.stm
- État, relation et suite : Titre/date/pertinence repérés; extraction échouée. Signature/images/audio inconnus. Comparer WRM S48 sans déduire relation de date commune.

### SUP-56 — Ten years Dzanga-Sangha Project: 1988–1999

- Date(s) rapportée(s) : 1999 selon références.
- Responsabilité / langue rapportée : A. Blom; World Wildlife Fund–Central African Republic/Bangui.
- Liens :
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC3465313/
  - https://ccsenet.org/journal/index.php/jsd/article/download/6344/5100
- État, relation et suite : Références bibliographiques, original non consulté. Période du titre ≠ année publication. Piste bilan institutionnel historique.

### SUP-58 — Rumbles in the jungle — article BBC Earth News

- Date(s) rapportée(s) : 3 mars 2010.
- Responsabilité / langue rapportée : BBC Earth News.
- Liens :
  - http://news.bbc.co.uk/earth/hi/earth_news/newsid_8546000/8546127.stm
- État, relation et suite : Page repérée sur recherche Dzanga Bai, extraction échouée. Relation au film DSC-025 à vérifier; article ≠ fiche/film.

### SUP-59 — 30 Jahre Dzanga-Sangha — dossier WWF Magazin

- Date(s) rapportée(s) : N° 02/2021.
- Responsabilité / langue rapportée : WWF Allemagne.
- Liens :
  - https://www.wwf.de/fileadmin/fm-wwf/Publikationen-PDF/WWF_Magazin/WWF-Magazin-0221-Dzanga.pdf
- État, relation et suite : PDF consulté, numéro visible. Gorilles, BaAka, droits, santé, écogardes, One Health. Photos notamment Thomas Nicolon, Miguel Bellosta, David Santiago García; signatures/pagination exactes à compléter. Coopération RKI depuis 2012 racontée, pas preuve de communication publiée en 2012.

### SUP-60 — Bulletin Décembre 2020 / Newsletter December 2020 — APDS

- Date(s) rapportée(s) : Décembre 2020; dépôts URL janvier/février 2021.
- Responsabilité / langue rapportée : APDS; français/anglais.
- Liens :
  - https://dzanga-sangha.org/wp-content/uploads/2021/02/12-Bulletin-Decembre-2020.pdf
  - https://dzanga-sangha.org/wp-content/uploads/2021/01/12-2020-DSPA-Newsletter-December.pdf
- État, relation et suite : Rétrospective 29 décembre 1990, Richard Carroll, Ndagbino Pascal/1987. Une édition mensuelle provisoire, versions à comparer, dates historiques ≠ bulletin.

### SUP-61 — Studying the world’s largest gathering of forest elephants with sound and field observation

- Date(s) rapportée(s) : 19 avril 2026.
- Responsabilité / langue rapportée : Entretien Ivonne Kienast; Rhett Ayers Butler et David Akana; Mongabay.
- Liens :
  - https://news.mongabay.com/2026/04/studying-the-worlds-largest-gathering-of-forest-elephants-with-sound-and-field-observation/
- État, relation et suite : Dzanga Forest Elephant Project/Cornell, suivi visuel-acoustique. Chiffres attribués à entretien et datés, pas indicateurs actuels automatiques.

### SUP-62 — A unique clearing in Central Africa draws elephants from the dense forests

- Date(s) rapportée(s) : 6 avril 2026.
- Responsabilité / langue rapportée : David Akana; Mongabay.
- Liens :
  - https://news.mongabay.com/2026/04/a-unique-clearing-in-central-africa-draws-elephants-from-the-dense-forests/
- État, relation et suite : Dzanga Bai, Kienast, tourisme; DOI annoncé 10.66709/news-317009. Article distinct entretien S61, comparer photos.

### SUP-63 — Central African Republic’s Dzanga-Sangha tests the promise of wildlife tourism

- Date(s) rapportée(s) : 31 juillet 2026.
- Responsabilité / langue rapportée : Rhett Ayers Butler; Mongabay Founder’s Briefs.
- Liens :
  - https://news.mongabay.com/short-article/central-african-republics-dzanga-sangha-tests-the-promise-of-wildlife-tourism/
  - https://changemakr.asia/central-african-republics-dzanga-sangha-tests-the-promise-of-wildlife-tourism/
- État, relation et suite : Analyse courte; visite terrain mars avec Akana; Gervais Pamongui/Léonce Madomi. Renvoie reportage long Akana à isoler. Changemakr 2 août = reprise pas nouvelle enquête.

### SUP-66 — Dzanga Sangha, une clairière en forêt vierge — crédits et ISAN

- Date(s) rapportée(s) : 1997/26 minutes secondaires; primaire date/durée non récupérées.
- Responsabilité / langue rapportée : Marie-Hélène Baconnet écriture/réalisation; Écomedia; Un jour dans la nature.
- Liens :
  - https://www.film-documentaire.fr/4DACTION/w_fiche_film/4776_0
  - https://www.composers21.com/compdocs/bosseurj.htm
  - https://www.faunesauvage.fr/fsrealisateur/baconnet-marie-helene
- État, relation et suite : ENRICHISSEMENT DSC-055. Fiche consultée: ISAN 0000-0001-8191-0000-6-0000-0000-J; France 2, Canal+ Belgique, Discovery Europe, RAI, TVE; CNC; Turkalo et Dzanga-Sangha dans synopsis. Année/durée à corroborer, ni VOD ni DVD établis. Accès Faune Sauvage échoué.

### SUP-67 — Los pueblos de elefantes — DW Transtel

- Date(s) rapportée(s) : 2010/30 min/AR ES EN à confirmer disposition catalogue.
- Responsabilité / langue rapportée : DW Transtel; référence 264702 014.
- Liens :
  - https://www.dw.com/downloads/38610625/04-la-lucha-por-la-supervivencianuevo.pdf
  - https://www.dw.com/downloads/50757004/dwtranstelprogramas201910.pdf
  - https://static.dw.com/downloads/57697508/dwtranstel-programas202104.pdf
- État, relation et suite : Synopsis Dzanga-Ndoki confirmé par catalogues; extraction fiche courte échouée, grand PDF partiel. Titre/référence piste solide; année durée langues encore partielles. Pas confondre catalogue 2019/2021 et production. Générique et relation autres films inconnus.

### SUP-68 — The wilderness and the war — DW

- Date(s) rapportée(s) : Page 16 janvier 2018; ajout évoquant enquête mai 2019.
- Responsabilité / langue rapportée : Jürgen Schneider, film et image présentation.
- Liens :
  - https://www.dw.com/en/the-wilderness-and-the-war/a-42147354
  - https://www.dw.com/en/wildlife-in-areas-of-armed-conflict/video-42109566
- État, relation et suite : ENRICHISSEMENT DSC-043. Page consultée: A film by Jürgen Schneider. Film/page/vidéo 5m14 (ancienne passation) à relier sans assimiler durées. Texte ultérieur sous page 2018, conserver mise à jour.

### SUP-69 — República Centroafricana: Protección de la naturaleza en tiempos de guerra / Naturschutz in Zeiten des Krieges

- Date(s) rapportée(s) : Espagnol index 13 mars 2019 vs titre extraction 20 décembre 2018; allemand index 10 mai 2019.
- Responsabilité / langue rapportée : DW; espagnol/allemand.
- Liens :
  - https://www.dw.com/es/rep%C3%BAblica-centroafricana-protecci%C3%B3n-de-la-naturaleza-en-tiempos-de-guerra/a-47897993
  - https://www.dw.com/de/naturschutz-in-zeiten-des-krieges/a-46072238
- État, relation et suite : Luis Arranz, Bayanga, Dzanga Bai, droits/santé. Version ES extraite avec mots tronqués: pas de citation exacte fondée là-dessus. Relation traduction/adaptation/article associé au film S68 à établir.

### SUP-70 — Fighting to save Africa’s biodiversity

- Date(s) rapportée(s) : 2013 selon bibliographie.
- Responsabilité / langue rapportée : Deutsche Welle.
- Liens :
  - http://www.dw.com/en/fighting-to-save-africas-biodiversity/a-17267827
  - http://rainforestparksandpeople.org/2017/03/23/dzanga_sangha-reference/
- État, relation et suite : Référence secondaire, original non consulté; format/durée/part Dzanga-Sangha non établis.
