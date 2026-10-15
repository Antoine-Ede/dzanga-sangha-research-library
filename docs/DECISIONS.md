# Décisions

## D001 — Active — Documents courts et rôles successifs (15 octobre 2026)

AGENTS est l’entrée commune, CLAUDE un renvoi. STATE contient le point de reprise, ROADMAP les priorités, les fiches le périmètre et les critères. Les anciennes fiches portent le statut « close » et une date ; pas de copie concurrente d’un état actuel. Aucun orchestrateur ou équipe permanente.

Spec Kit a été évalué sur son [guide officiel d’adoption dans un projet existant](https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md), consulté le 15 octobre : il ajoute notamment des fichiers `.specify` et des commandes d’intégration. Le besoin actuel est couvert par deux fiches et une commande. Les conversations sur les autres projets suggèrent des bénéfices possibles, mais ne constituent pas une expérimentation comparée sur cette bibliothèque. Pas d’installation ; réévaluer pour une évolution transversale dont le suivi manuel devient insuffisant.

## D002 — Active — Déterminisme avant fournisseur IA (15 octobre 2026)

Python standard + SQLite suffisent pour identités, provenance, conflits, reprises et décisions. [Pydantic AI](https://pydantic.dev/docs/ai/core-concepts/output/) fournit des sorties structurées et des [modèles de test](https://pydantic.dev/docs/ai/api/models/test/) ; sources officielles consultées le 15 octobre. Ce n’est pas une preuve de vérité bibliographique. Pas de gain mesuré ici face à un schéma explicite et un fournisseur simulé, donc aucune dépendance Pydantic AI ni fournisseur réel ajouté. Une future comparaison devra mesurer exactitude des propositions sourcées, abstentions, coût et temps de revue sur un jeu public validé.

Aucune donnée n’est transmise à une IA dans ce prototype. Une future intégration devra préciser fournisseur, champs/extraits publics envoyés, rétention, plafond de coût et accord spécifique. Le mode sans clé reste obligatoire.

## D003 — Active — Propositions locales, catalogue en lecture (15 octobre 2026)

La découverte Crossref et l’instantané Zotero utilisent uniquement GET, hôtes fixes HTTPS, délais et reprises bornés. La requête publique est transmise à Crossref ; seul l’identifiant du groupe et la pagination le sont à Zotero. Ni document privé, ni PDF, ni clé. Le cache et les décisions sont locaux et ignorés par Git. Les autres sources passent d’abord par une entrée JSON explicitement publique. Aucune publication ou écriture Zotero n’existe dans la CLI.

Une identité DOI normalisée permet un regroupement technique avec conservation des contradictions. Une ressemblance de titre reste une suggestion sans fusion. Aucune probabilité scientifique. Une décision « retenir » signifie conserver dans le parcours de revue, pas référence scientifiquement validée ni contenu autorisé à la diffusion.

L’essai public du 15 octobre a ramené des faux positifs évidents avec la recherche bibliographique large. La recherche sur titre est donc le défaut de ce premier parcours ; le mode large reste explicite. Les deux modes conservent la requête et leurs curseurs séparément. Ce choix réduit le bruit observé sans garantir la pertinence ni une couverture exhaustive. Pagination et pauses suivent les [conseils Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/) et les [principes de l’API Zotero](https://www.zotero.org/support/dev/web_api/v3/basics).

## D004 — Active — Préservation APDS (15 octobre 2026)

Conserver les conventions `SCOPE:`, `STATUS:`, `ACCESS:` et les preuves `Scope evidence:` existantes. Les champs du prototype complètent ce modèle, sans migrer Zotero ni les instantanés historiques. Pas de nouveau PDF ; les six copies publiques restent inchangées. Pour toute revue future : auteurs ≠ signataires, date de publication ≠ terrain/signature, copie publique ≠ original/OCR ; conserver les lacunes et les retraits déjà effectués.

## D005 — Active — Tri documentaire proportionné (15 octobre 2026)

Demande utilisateur : ne plus imposer l'ouverture de chaque page pour décider du traitement initial d'un document. Cette décision remplace cette exigence systématique dans les étapes de reprise, sans invalider les contrôles antérieurs.

Premier niveau : identité et version, nature du document, couverture/sommaire/introduction/conclusion disponibles, recherche dans l'OCR et pages ciblées pour les auteurs, dates, pertinence et alertes. Résultat distinct : notice seule, candidat PDF public, copie à expurger, ou accès encadré. Une recherche de mots-clés seule ne certifie pas l'absence de contenu sensible ; consigner ce qui a été effectivement examiné et la qualité de l'OCR.

Approfondissement ciblé si cartes détaillées, signatures, listes nominatives, données personnelles, informations opérationnelles ou OCR insuffisant ; étendre le contrôle si la nature du document le justifie. Les parties non examinées restent explicitement non certifiées. Ne pas ajouter artificiellement les pages au compteur de lecture intégrale. Une copie expurgée nécessite le contrôle des retraits, du texte récupérable et des éléments incorporés ; une vue d'ensemble/échantillonnage ne prouve pas une expurgation complète.

L'absence de DOI ne détermine ni sensibilité ni droit de diffusion. Objectif demandé : conserver les PDF APDS appropriés comme pièces jointes Zotero et rendre une version autorisée accessible depuis le site. L'original sensible peut rester en consultation encadrée tandis qu'une copie publique existe. Stockage Zotero, téléchargement anonyme et licence de redistribution sont trois vérifications distinctes. Le groupe est PublicClosed avec stockage membres activé d'après GET du 15 octobre ; la [documentation Zotero](https://www.zotero.org/support/groups) décrit le partage de fichiers entre membres : un accès anonyme depuis Pages doit être éprouvé, pas supposé. Ne jamais exposer une clé dans le site pour le permettre.
