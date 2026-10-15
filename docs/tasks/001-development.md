# Lot 1 — développement et reprise

Statut : close localement le 15 octobre 2026. Responsable : session Codex, un seul écrivain.

- Besoin : réduire pertes de décisions, dérive de périmètre et validations non démontrées.
- Périmètre : points d’entrée communs, état, décisions, fiches, contrôles locaux reproductibles. Exclusions : configuration globale, hooks, CI distante, modification d’interface, fournisseur IA.
- Acceptation : une commande hors ligne ; preuve liée à HEAD et aux fichiers/index réellement testés ; preuve refusée après modification ; secrets/fichiers interdits détectés ; instantanés APDS conservés ; rôles et limites de validation explicites.
- Règles : catalogue Zotero intact, originaux privés hors Git, un écrivain, aucune action distante d’écriture.
- Fichiers : AGENTS, CLAUDE, README, docs, ROADMAP, tools/check.py, tests, .gitignore et configuration des contrôles.
- Validation : tests synthétiques autorisés/refusés, régression de rendu existante portée dans le dépôt ; syntaxe et empreintes des artefacts publics. Pas de prétention de contrôle scientifique ou publication.
- Risques : faux négatifs du scanner, preuve périmée, duplication documentaire. Retour : commit distinct annulable et checkout initial intact ; preuves locales sauvegardées avant nettoyage.
- Revue : même session. Tests du scanner (fichiers autorisés/interdits, index différent du fichier), péremption de preuve, syntaxe et rendu synthétique exécutés via le contrôle commun. Les différences CRLF de Git sont tolérées pour la comparaison historique des textes, pas pour les empreintes de preuve ni les binaires. Aucune interface modifiée, donc pas de revue utilisateur requise pour ce lot.
- Suite : lot 2, sans élargissement à un tableau de bord.
