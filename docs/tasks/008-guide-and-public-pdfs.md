# Lot 008 — mode d'emploi et contrôle des PDF publics

Statut : réalisée et vérifiée, revue utilisateur acceptée le 17 octobre après l'aperçu et la proposition de fusion ; intégration PR 6 suivie dans le lot 009. Session Codex.

- Besoin : livrer le guide resté sur une ancienne branche et confirmer que les archives dont une copie publique est déjà validée sont accessibles via leur PDF.
- Périmètre : porter le guide sur le main actuel, documenter l'ouverture des PDF, vérifier les six copies publiques du manifeste sans connexion et par empreinte.
- Exclusions : aucun nouvel original publié, aucune expurgation ou correction des notices d'archives ; le chantier APDS parallèle continue séparément. Aucun secret dans le site.
- Acceptation : onglet Mode d'emploi fonctionnel, lien profond, maintien des filtres, accessible même en cas d'erreur Zotero ; recherche/statistiques/export masqués dans le guide ; dernières fonctions des notices/PDF conservées ; six liens publics conformes au manifeste ou écart explicite.
- Fichiers : app.js, index.html, styles.css, tests/browser.cjs, STATE, fiche et preuve publique des six liens.
- Validation : commande commune, test navigateur desktop/mobile et erreur API ; contrôle public distinct des PDF réels. Auto-revue, pas de revue indépendante. Revue utilisateur de l'interface avant fusion.
- Retour : commit distinct annulable ; checkout de l'ancien guide et travaux parallèles préservés. Aucun changement Zotero prévu.
- Suite : PR séparée du bilan bibliographique nº 5 ; ne pas confondre ouverture de PR et fusion/publication.

Résultats : guide porté depuis f04245a sur main fb60b78, conflits de styles, protection des fichiers locaux et versions de cache réconciliés en conservant les évolutions PDF/notices. Tests du lien profond, clavier, retour avec recherche conservée, mobile et API 403 réussis ; captures desktop/mobile inspectées. Contrôle commun : 34 tests Python, syntaxe, rendu et navigateur. Détecteur Impeccable : trois alertes sur les styles préexistants (en-tête, palette, avertissement), aucune nouvelle règle du guide signalée ; identité visuelle conservée. Aucun audit complet WCAG ou lecteur d'écran revendiqué.

Contrôle public indépendant des fixtures : six notices uniques, six GET anonymes HTTP 200, signatures PDF et tailles/SHA-256 identiques au manifeste. Le serveur renvoie application/octet-stream, donc le lien peut télécharger le fichier ; ne pas promettre de lecteur intégré. Aucun changement Zotero, document ou manifeste nécessaire. Preuve versionnée dans docs/verification/public-plans-2026-10-16.json.
