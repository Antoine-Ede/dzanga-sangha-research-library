# Intégration et cadrage des suites demandées

Statut : préparation de l'intégration ; résultat de livraison dans STATE et preuve locale. 15 octobre 2026.

- Besoin : intégrer le socle validé à main au moment opportun et conserver les nouvelles demandes, sans transformer ce lot en refonte de l'interface.
- Autorisation : demande explicite « fusionne main au moment le plus opportun ». Inclut publication de la branche, PR et fusion après contrôles, ainsi que Pages déclenché par main. Pas d'écriture Zotero ni de planification activée ici.
- Périmètre : actualiser AGENTS, DECISIONS, ROADMAP, STATE ; diagnostiquer les deux exemples sur code et métadonnées publiques ; premières pistes historiques sourcées ; sauvegarde et intégration du socle/prototype existants.
- Exclusions : correction en masse des auteurs, refonte des notices, indicateurs d'accès, téléversement des PDF, nouveau connecteur ou lancement semestriel. Ces demandes sont des suites explicites dans ROADMAP, pas des réalisations annoncées.
- Critères : les six demandes figurent au suivi avec critères observables ; aucune page non lue déclarée auditée ; aucune donnée privée ajoutée ; contrôles communs réussis avant fusion ; SHA fusionné contrôlé ; état du déploiement distingué du test local.
- Fichiers : cinq documents ci-dessus, plus cette fiche ; code du site et catalogue inchangés.
- Validation : tests existants (34 Python et rendu JavaScript synthétique), différences/empreintes/secrets ; GET publics pour l'exemple d'auteur et configuration Zotero ; références historiques consultées. Auto-revue, pas de revue indépendante ; aucun changement d'interface nécessitant une nouvelle revue utilisateur.
- Risques/retour arrière : bundle Git vérifié avant publication ; conserver worktrees et fichiers ignorés ; revert des commits de fonctionnalité ou de la fusion après vérification, sans reset ni effacement de l'historique. Aucun effet Zotero à annuler.
- Suite recommandée : premier petit lot sur la qualité des auteurs et la présentation des informations d'archive, puis pilote PDF accessible anonymement.
