# Procédure locale proportionnée

1. **Coordination** : lire STATE, contrôler Git et le périmètre ; ouvrir une fiche pour un changement significatif. Toute autorisation distante doit être actuelle et explicite.
2. **Développement** : un écrivain par worktree, petits lots réversibles. Conserver les sources et décisions existantes.
3. **Revue critique** : relire le diff en cherchant défauts, régressions et preuves manquantes. Une auto-revue reste une auto-revue. Après deux corrections infructueuses, revoir le diagnostic avant une nouvelle tentative.
4. **Contrôle exécuté** : `python tools/check.py`. Cette commande inspecte syntaxe Python et JavaScript, tests métier, inventaire public, empreintes des copies publiques, différences Git et fichiers/chaînes interdits. Aucun accès Internet n'est nécessaire ; le test navigateur utilise uniquement un serveur local éphémère et des réponses Zotero fictives.
5. **Revue utilisateur** si interface : contrôle navigateur avec données fictives et revue du parcours, clavier, libellés, erreurs et accessibilité. Décrire le scénario et les limites. Le contrôle navigateur doit être ajouté au point d’entrée avant d’accepter une modification d’interface ; en son absence le contrôle commun refuse ces changements.
6. **Reprise** : mettre à jour STATE et statut de la fiche, puis relancer le contrôle sur l’état final. Un commit supplémentaire change HEAD : relancer avant d’annoncer la validation de ce SHA.

## Portée de la preuve

`.local/verification.json` contient commit, base, statut Git, SHA-256 des fichiers versionnés et non ignorés, différences indexées/non indexées, versions des outils, commandes, codes de sortie et sorties. Une empreinte avant/après détecte aussi les modifications pendant le contrôle. `python tools/check.py --verify-proof` refuse un changement de HEAD, d’index, de fichier ou de statut. Cela inclut les documents de suivi.

Les données de travail ignorées ne sont pas certifiées par cette preuve de code ; un essai sur données réelles doit avoir son propre rapport avec empreinte et provenance des entrées. Les tests sont synthétiques sauf indication contraire. Aucune validation scientifique, autorisation de diffusion ou publication ne découle de leur réussite.

Le contrôle d'interface lance désormais `tests/browser.cjs` via le Node résolu par la commande commune (`{node}` dans `.checks.json`). Il utilise Playwright déjà installé dans le projet ou le runtime Codex, et Chrome installé sous Windows ou le navigateur Playwright disponible ailleurs. Aucune installation/téléchargement automatique ; une dépendance manquante fait échouer le contrôle. Le serveur n'écoute que sur loopback, les routes de fichiers sont explicitement limitées et les appels Zotero sont simulés. En environnement sandbox, l'accès local au navigateur peut nécessiter une permission d'exécution supplémentaire ; ne pas transformer cet échec en réussite. Captures et résultat : `.local/browser/`. Le parcours contrôle clavier, trois vues, mobile, recherche/filtres, analyse, qualité et export ; il ne constitue pas un audit complet par lecteur d'écran. La revue utilisateur reste distincte.

La détection de secrets combine motifs connus et chemins interdits. Elle ne reconnaît pas tous les secrets ni les informations personnelles d’un texte ou d’une image. Relecture humaine obligatoire avant ajout de nouveaux documents ; les PDF publics préexistants sont autorisés seulement à empreinte inchangée. Aucune installation de hook : pas de fausse impression de barrière complète, aucune modification globale.

## Retour arrière

Les deux lots sont des commits locaux distincts. Pour les abandonner, conserver d’abord la base de propositions et les preuves locales, puis revenir au checkout initial intact ; ne pas supprimer un worktree contenant des fichiers non sauvegardés. Pour un retour sélectif, utiliser `git revert` du commit concerné après vérification du statut. Ne pas appliquer automatiquement de reset ou de nettoyage.

Les scripts privés historiques restent à leur place. Leur ancien SHA ou nom de branche dans une assertion est un contexte historique, pas une instruction de restaurer cet état.
