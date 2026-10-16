# Pilote d'accès PDF APDS

Statut : interface locale réalisée ; téléchargement public vérifié ; stockage Zotero vérifié ; revue utilisateur et publication restantes. Branche `codex/library-pdf-access`, base `3ee16aa`.

- Besoin : ouvrir un PDF de diffusion depuis chaque présentation, séparément de sa notice Zotero.
- Périmètre : lien explicite pour les URL de documents finissant en `.pdf` ; pilote réel APDS-069 Bayanga, copie publique expurgée préexistante, notice NJ4EAIJT. L'accord utilisateur « ok continue » autorise son stockage ciblé dans Zotero lorsqu'un accès d'écriture est disponible.
- Exclusions : aucun original, changement de droits, correction d'auteurs ou import général ; pas de récupération automatique de toutes les pièces jointes. DOI et catalogue restent inchangés.
- Acceptation : lien dans les trois vues, distinct de Notice Zotero, utilisable au clavier ; aucun lien PDF inventé pour une notice sans URL PDF ; avertissement sur l'original conservé ; SHA du PDF public identique au manifeste ; stockage Zotero et accès anonyme démontrés séparément.
- Fichiers : app.js, styles.css, index.html, tests/site.cjs, tests/browser.cjs, fixture fictive ; STATE/ROADMAP.
- Validation : commande commune, tests synthétiques des trois vues et navigation clavier ; GET public sans authentification du PDF réel avec contrôle SHA-256. Le test navigateur simulé ne valide pas le lecteur PDF ni les droits.
- Risques : URL publique devenue inaccessible, stockage Zotero réservé aux membres, confusion original/copie. Conserver l'URL publique immuable existante comme accès complémentaire ; ne pas inclure de clé dans le site.
- Retour arrière : revert du lot local ; main et anciens worktrees préservés. Avant ajout distant, sauvegarder notice/version et enfants, vérifier l'absence de doublon. Aucun effacement distant automatique.
- Revue : même session, pas de revue indépendante ; aperçu pour revue utilisateur avant publication.

Résultats : tests synthétiques et navigateur réussis ; téléchargement réel sans connexion conforme au SHA du manifeste Bayanga. Le serveur public déclenche un téléchargement, pas une lecture intégrée. Notice version 938 sans enfant lors du GET préalable ; copie expurgée jointe sous CM5RDMRW avec la clé fournie ensuite. Retéléchargement authentifié conforme au SHA-256, parent inchangé. GET du fichier Zotero anonyme : 404 ; URL publique complémentaire conservée. Preuves locales et reprise détaillées dans STATE. Les deux registres d'audit et la base/export des décisions antérieures ont conservé leurs empreintes du lot 20.
