# Skills utilisés pour la revue bibliographique

Trois skills ont été sélectionnés sur les annuaires Skills.sh et les dépôts académiques, examinés puis installés le 14 octobre. Les annuaires servent à la découverte ; les instructions viennent des dépôts d'origine à des commits fixes.

| Skill | Origine figée | Usage |
| --- | --- | --- |
| citation-management 2.3 | K-Dense-AI/scientific-agent-skills, a1043ef544e3a100c28e70a736b6cf32554d0677 | Recherche PubMed et recoupement des métadonnées DOI avec les originaux. |
| scientific-critical-thinking 1.5 | Même dépôt et commit | Distinguer observation, association et causalité ; apprécier les limites dans le contexte du document. |
| paper-reading | jxtse/scientific-research-skills, 68098d5565f423ffcfce1c9936de77ae230843aa | Lecture proportionnée : sites, méthodes, tableaux et alertes avant approfondissement. |

Liens : [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills), [paper-reading](https://github.com/jxtse/scientific-research-skills), [Skills.sh](https://skills.sh/).

Les empreintes des instructions examinées sont conservées dans le rapport local d'installation. Aucun service IA payant, serveur Zotero supplémentaire, hook ni envoi de PDF privé n'a été activé. Les dépendances du client PubMed ont été isolées dans l'espace de recherche local ; le runtime partagé n'a pas été modifié. Le client de recherche publique n'utilise pas les identifiants Zotero.

La revue du [16 octobre](../reviews/pubmed-2026-10-16/README.md) illustre leur application : une affiliation APDS ne suffit pas à classer Core ; une analyse utilisant des échantillons APDS négatifs peut en revanche relever de Core. Les métadonnées et droits d'accès sont vérifiés séparément. La validation d'un JSON ou d'un import n'établit pas la vérité scientifique.

Crédit méthodologique demandé par les skills K-Dense : Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents*. [arXiv:2609.00065](https://doi.org/10.48550/arXiv.2609.00065), version 2 vérifiée le 14 octobre. Ce crédit concerne l'outillage logiciel ; il n'ajoute pas de référence hors périmètre au catalogue Zotero.
