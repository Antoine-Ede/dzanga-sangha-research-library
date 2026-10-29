# Tâche 020 — Réception et rapprochement du supplément Communication

Statut : conservation et rapprochement hors ligne terminés ; vérification des sources ouverte. Date : 25 octobre 2026. Responsable : assistant.

- Besoin : recevoir le Markdown de la session Communication parallèle annoncé par l'utilisateur, le préserver et comparer ses entrées aux registres existants.
- Copie/branche : library-current-main, research/communication-register-recovery-2026-10-24, base de reprise c81465c. Autres worktrees et branches préservés.
- Périmètre : 70 blocs SUP et liens, provenance, rapprochements documentaires et instantané Zotero local. Aucun import, écriture Zotero, push, fusion ou déploiement. Aucune nouvelle recherche web directe ; recherches supplémentaires uniquement via Perplexity.
- Critères : identifiants complets et uniques, restitution exacte des blocs après lecture TSV, original privé avec empreinte, déclarations séparées des preuves et rapprochements. Aucune somme annoncée comme nombre d'œuvres nouvelles.
- Règles : versions, index, composantes et éditions distincts ; pas d'identité par seul titre ; pas de généralisation géographique ; pas de téléchargement exclusif SUP-39 ou reprise d'audit APDS.
- Validation : contrôle de couverture/structure/empreintes, comparaison des registres existants sans modification, diff indexé, tools/check.py puis preuve fraîche sur SHA final.
- Revue : auto-revue hors ligne de la même session, limites d'absence de vérification actuelle des sources et du catalogue explicites.
- Retour arrière : retirer seulement le commit documentaire concerné en conservant source privée et premier registre ; aucun catalogue à restaurer.
- Prochain pas : premier commit de conservation, puis rapprochements hors ligne et priorités ciblées.

- Conservation réalisée au commit 6c581e7 : 70 blocs et 101 liens, round-trip exact et empreinte du document contrôlés. Contrôle commun passé sur le SHA de conservation.
- Rapprochement calculé : sept entrées avec URL correspondante dans l'instantané complet du 24 octobre, 63 sans correspondance exacte ; 12 candidats locaux, cinq enrichissements DSC rapportés, aucune fusion. Sept alertes documentées. Aucun de ces rapprochements n'atteste une consultation actuelle de source.
- Livrable : reviews/communication-supplement-2026-10-25/RECONCILIATION.md et registres liés. Le fichier reçu est archivé et le suivi COMM-EXTERNAL marqué reçu, sans lecture de la session externe. Aucune recherche web, écriture Zotero ou publication.
- Suite : vérifications ciblées via Perplexity, en priorité CARPO/SUP-65, National Geographic/SUP-64 et presse1994/SUP-51 ; aucune autorisation d'import.

## Consolidation du 29 octobre

Deux missions du 25 octobre : six entrées examinées, une confirmation déléguée (SUP-51), quatre partiels, un blocage ; 64 entrées non examinées dans ces missions. Réponse en attente récupérée depuis le DOM visible, sans relance des recherches. Voir PRIORITY-REVIEW.md. Aucune correction Zotero, aucun import/push/déploiement ; originaux et anciens registres inchangés. Contrôles de structure, identifiants et empreintes puis contrôle commun requis sur le commit final.

## Mesure de délégation — 29 octobre

Un outil local compte les missions, cas, artefacts, volumes textuels et seules durées affichées dans les preuves privées. Il ne convertit pas des mots en jetons et ne calcule aucun gain sans export d'usage fournisseur et comparaison directe équivalente. La mesure actuelle est donc un indicateur de volume et de couverture, jamais une économie démontrée. Voir `docs/PERPLEXITY_MEASUREMENT.md`.
