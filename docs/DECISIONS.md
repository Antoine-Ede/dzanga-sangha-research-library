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

## D004 — Active — Préservation APDS (15 octobre 2026)

Conserver les conventions `SCOPE:`, `STATUS:`, `ACCESS:` et les preuves `Scope evidence:` existantes. Les champs du prototype complètent ce modèle, sans migrer Zotero ni les instantanés historiques. Pas de nouveau PDF ; les six copies publiques restent inchangées. Pour toute revue future : auteurs ≠ signataires, date de publication ≠ terrain/signature, copie publique ≠ original/OCR ; conserver les lacunes et les retraits déjà effectués.
