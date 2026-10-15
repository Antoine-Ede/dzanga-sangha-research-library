# Lot 2 — file locale de propositions

Statut : close pour le prototype local ; revue scientifique humaine restante. Date : 15 octobre 2026. Responsable : même session Codex.

- Besoin : découvrir des candidats sourcés, les comparer au catalogue et préparer une revue humaine sans écrire dans Zotero.
- Périmètre : CLI Python standard, Crossref public + entrée JSON publique, instantané Zotero en lecture, SQLite local, export JSON et décisions explicites. Fournisseurs déterministe et simulé uniquement.
- Exclusions : imports Zotero, PDF/OCR privés, IA réelle, traitements planifiés, nouveau tableau de bord, attribution automatique Core.
- Acceptation : relance idempotente ; décisions conservées ; absence de DOI acceptée ; conflits visibles ; faux rapprochement de titre non fusionné ; pagination et reprise après erreur sans perte ; réponse invalide refusée ; sans clé ; sortie simulée sans preuves refusée ; propositions jamais étiquetées comme références validées.
- Règles : provenance champ par champ, lacunes précises, séparation découverte/pertinence/métadonnées/diffusion ; conservation des conventions APDS et des sources.
- Fichiers : tools/biblio/, tools/bibliography.py, tests, fixtures fictives, guide d’utilisation ; aucun fichier du site ou catalogue historique modifié.
- Validation : tests unitaires et parcours CLI sur fixtures, puis essai limité en GET sur métadonnées publiques avec rapport distinct si réseau disponible.
- Risques : Crossref incomplet pour les archives, erreurs déposées, curseurs expirés, catalogue changeant ; signaler fraîcheur et limites. Reprise transactionnelle ; sauvegarde SQLite avant intervention manuelle.
- Retour : lot séparé annulable ; conserver la base locale avant retrait des outils.
- Revue : même session, recherche de défauts après réalisation ; revue humaine bibliographique réelle reste à effectuer.

Résultats : critères techniques couverts par les tests dans la commande commune (32 tests Python au total pour les deux lots), parcours CLI fictif et essai GET public distinct, décrits dans STATE. Un changement de preuve ou de catalogue demande un réexamen sans effacer la décision. Les pauses serveur survivent aux relances. Le site, Zotero et les documents APDS ne sont pas modifiés. Preuves exactes locales : `.local/verification.json` et `.local/public-smoke-report.json` ; vérifier leur SHA et fraîcheur avant réutilisation.

Reste : revue humaine de pertinence/identité sur les candidats réels, évaluation de la couverture des sources sans DOI et des thèses, mesure de l’utilité des enrichissements avant toute IA réelle. Aucun examen des droits des PDF ni validation scientifique réalisé par ce lot. Le rapprochement toutes paires de la petite file n’est pas optimisé pour un très grand corpus.
