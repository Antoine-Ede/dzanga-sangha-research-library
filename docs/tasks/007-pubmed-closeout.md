# Lot 007 — clôture de la revue PubMed

Statut : close, livraison Git en préparation. 16 octobre 2026, session Codex bibliographie.

- Besoin : terminer la sélection PubMed commencée le 14 octobre, en tenant compte des imports et du nouveau socle de développement.
- Périmètre : dix candidats encore en attente ; vérifier identité et preuve territoriale, importer seulement les références confirmées absentes, contrôler la relance et consigner les limites. La demande du responsable du 16 octobre fournit une authentification locale pour terminer ce travail. Elle n'étend pas le pilote PDF du lot 006.
- Exclusions : archives APDS, pièces jointes, correction des auteurs des archives, modification de l'interface, automatisation et import des instantanés historiques.
- Acceptation : chaque candidat reçoit une décision motivée ou un blocage documentaire explicite ; aucun doublon ; lecture après chaque écriture ; audit final public ; preuve locale du dépôt. Aucun secret ou PDF d'éditeur ajouté au dépôt.
- Base : origin/main fb60b78 ; worktree isolé, checkout du guide conservé. Audit public initial : 427 références, 19 collections, seed 31/31, zéro titre vide ou doublon détecté. Le lot précédent de six est déjà présent.
- Fichiers : dossier de revue public, documentation de reprise et STATE ; scripts d'import conservés dans l'espace de recherche local et identifiés dans le bilan.
- Validation : métadonnées DOI et sources originales ciblées ; prévalidation, import et relance sur Zotero public ; commande commune hors ligne. Ces contrôles n'équivalent pas à une revue scientifique indépendante ou exhaustive.
- Risques et récupération : sauvegarde avant toute modification d'une notice ; aucune suppression prévue. Créations traçables par DOI et clé ; ne pas annuler une notice ayant reçu des enrichissements ultérieurs sans inspection.
- Résultat : dix décisions closes (8 acceptations, 2 exclusions révisables) ; huit créations vérifiées publiquement, une pagination complétée avec sauvegarde et version ; relance : zéro création, huit déjà présentes, zéro correction supplémentaire. 435 références après, 19 collections, seed 31/31, aucun titre vide ni doublon détecté.
- Validation : prévalidation Crossref/Zotero et exécution sous Windows PowerShell 5.1 ; contrôles publics et relance réelle. Commande commune : 34 tests Python, syntaxe JavaScript, rendu synthétique et navigateur passent. Premier lancement navigateur en sandbox impossible faute de binaire visible ; relance avec accès au navigateur installé réussie, sans installation. La preuve finale est régénérée après commit.
- Revue : même session, aucune revue indépendante revendiquée. Le texte intégral de Flahou reste non confirmé, sans tag d'accès inventé. Les exclusions n'affirment pas une absence absolue de données APDS.
- Suite : reprendre un lot de découverte distinct, sans relancer les CSV historiques. Les archives et le guide en branche préexistante sont conservés séparément.
