# Tâche 019 — Récupération du registre et recherche historique

Statut : conservation terminée ; première passe historique documentée, corpus restant ouvert. Date : 24 octobre 2026. Responsable : assistant.

- Besoin utilisateur : lire la passation, préserver d'abord les pistes sur une branche dédiée, contrôler et créer un commit documentaire, puis poursuivre la recherche historique.
- Base : main à `a444984a9fd40c7ea8f7c76bcb85e3c3c911c1ad`, copie propre ; branche `research/communication-register-recovery-2026-10-24`. Ne pas modifier les anciennes branches Perplexity ni les autres worktrees.
- Périmètre : métadonnées, liens, provenance et décisions documentaires. Exclusions explicites : aucun import/écriture Zotero, aucune fusion à main, aucun déploiement sans accord. Aucun original APDS ni œuvre protégée republié.
- Critères : 60 identifiants source conservés avec réserves ; registres distincts pour déclarations, consultations vérifiées et rapprochements Zotero ; premier commit de conservation avant recherche ; puis sources historiques primaires/catalogues et nouvelles pistes documentées. Toute impossibilité technique reste distincte d'un rejet scientifique ou d'un document disparu.
- Règles : ne pas attribuer DSPA-Core aux médias ; aucune indépendance journalistique exigée ; dates et langues qualifiées ; œuvres, traductions, extraits, galeries et sons de terrain distincts ; absence de DOI non problématique.
- Fichiers : `reviews/communication-discovery-2026-10-24/`, STATE et cette fiche. Aucun changement d'interface.
- Validation : unicité/couverture des identifiants, relecture des blocs conservés contre la passation, champs de preuve non remplis artificiellement, lecture complète de la pagination Zotero seulement, `git diff --cached --check`, contrôle commun et preuve sur le SHA final.
- Risques/retour arrière : erreurs conversationnelles conservées comme telles, liens fragiles et versions confondues. Deux commits documentaires séparant conservation et résultats, réversibles sans toucher au catalogue ni aux fichiers privés.
- Revue : auto-revue dans la même session, aucune revue indépendante revendiquée. Les pages non consultées et les œuvres non visionnées restent indiquées.
- Conservation : commit `292fe926c1e7eea2b972a400d5cb10a150545428`, contrôle commun passé avant et après commit. Les 60 blocs rapportés sont inchangés dans la suite.
- Résultats : 17 identifiants initiaux consultés, 15 avec métadonnées confirmées ; dix nouvelles entités historiques dont sept avec métadonnées documentées. 22 lignes de métadonnées au total, sans les assimiler à des œuvres indépendantes. Cinq rapprochements Zotero confirmés sur pagination complète publique (458 références), aucune écriture.
- Livraison : deux commits documentaires locaux ; contrôle commun et preuve fraîche sur le SHA final dans `.local/verification.json`. Registre et preuves privées préservés, aucune publication induite. Bilan détaillé : `reviews/communication-discovery-2026-10-24/HISTORICAL-REVIEW.md`.
- Prochaine étape : originaux Boston Phoenix/Natural History/National Geographic, catalogues AMNH et identités des montages BBC/RTVE. 43 pistes initiales sans consultation dans cette passe ; aucun achèvement global revendiqué. Import ou déploiement uniquement après nouvel accord.

## Extension du 25 octobre — délégation et suivi

À la demande utilisateur : recherches web supplémentaires exclusivement via Perplexity ; suivi de l'état et des exports dans une discussion dédiée, sans toucher à la session Communication externe. Livrables : `docs/PERPLEXITY_WORKFLOW.md`, `tools/perplexity_handoff.py`, tests fictifs et registre privé des missions. Test réel : réponse finale collectée et inventoriée avec empreinte ; artefact proposé mais téléchargement non confirmé. Trois cas partiels/deux bloqués, aucune source nouvellement promue. Aucun import/déploiement/push. Revue dans la même session ; pas de synchronisation ou de relecture indépendante revendiquée. Contrôle commun et preuve fraîche requis sur le prochain commit local.
