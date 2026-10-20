# Tâche 016 — liens des sources officielles

Statut : vérification technique terminée, revue utilisateur requise avant fusion. Responsable : assistant, 20 octobre 2026.

- Besoin utilisateur : renvoyer vers le dépôt officiel même lorsque le texte intégral n'est pas confirmé.
- Périmètre : six URL de notices hors archives ; notice HAL exacte pour Diallo et adresses éditeur déposées dans Crossref pour cinq articles. Le contrôle public a révélé que la vue Tableau masquait les URL complémentaires hors PDF : afficher cette source dans les trois vues, avec « Notice HAL » ou « Source en ligne », séparée de « Notice Zotero ». Aucun audit APDS, import, fichier PDF ou changement des règles de qualité.
- Critères : identité par DOI et titre, source officielle et nature du lien consignées ; aucune disponibilité gratuite déduite du seul lien ; sauvegarde, version conditionnelle, autres champs préservés et relance sans écriture.
- Fichiers : app.js, styles.css, tests synthétiques ; bilan public `reviews/official-source-links-2026-10-20/`, STATE et ROADMAP ; scripts et sauvegardes privés conservés dans les dossiers locaux existants.
- Validation : prévol public des six notices, lectures publiques après correction, comparaison du catalogue avant/après, contrôle de relance, audit bibliographique et navigateur public. Contrôle commun du dépôt pour le bilan. Auto-revue dans la même session, pas de revue indépendante.
- Risques et retour arrière : lien de notice confondu avec PDF ; erreur technique confondue avec restriction ; changement concurrent. Restaurer uniquement URL/Extra depuis les sauvegardes après comparaison des versions actuelles.
- Résultat : six URL/Extra corrigés, sauvegardes et lectures publiques ; relance zéro écriture, six conformes. Toutes les autres données des notices identiques, dont archives APDS et tags d'accès. Audit complet conforme, 435 références et compteur 122 inchangés.
- Vérifications : contrôle commun réussi, dont ouverture clavier du lien complémentaire et maintien des liens DOI/PDF/Zotero dans les trois vues ; tests de rendu sans réseau et tests navigateur synthétiques incluant mobile. Aperçu local sur données Zotero publiques réelles : lien HAL exact, titre DOI et notice Zotero distincts. Capture locale conservée. Détecteur Impeccable : seul avertissement sur la bordure d'archive préexistante, hors de ce correctif ; aucune refonte ajoutée.
- Prochaine étape : revue utilisateur de l'affichage, puis fusion si autorisée. Les incertitudes d'accès, les deux liens de thèses et la date FTNS sont conservés. Rien de nouveau à importer.
