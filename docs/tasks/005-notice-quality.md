# Notices d'archives compactes et auteurs à vérifier

Statut : réalisation locale achevée, revue utilisateur en attente ; contrôle final à lire dans `.local/verification.json`. 16 octobre 2026. Branche : `codex/library-notices-quality`, base `807dfc4`.

- Besoin : alléger les notices répétitives et traiter l'exemple d'auteur « A », sans abandonner la curation APDS.
- Périmètre : résumé d'archive concis dans les trois vues, détails complets repliables, signalement prudent des noms réduits à des initiales ; proposition locale sourcée pour les treize créateurs de l'exemple.
- Exclusions : aucune permutation automatique du catalogue, aucune écriture Zotero, aucun PDF ajouté ; audit APDS, pilote PDF, histoire et veille restent suivis dans ROADMAP. Pas de fusion de ce lot avant revue utilisateur de l'interface.
- Acceptation : provenance et lacunes visibles une seule fois dans le résumé, avertissements conservés, détails intacts ; aucune inférence d'auteur ni de droit de diffusion ; filtre/recherche/analyse/qualité et clavier opérationnels ; conservation des auteurs institutionnels et noms courts ; tests et preuve sur le commit final.
- Fichiers : app.js, library-model.js, index.html, styles.css si nécessaire, tests/site.cjs, tests navigateur et commande commune ; STATE/ROADMAP.
- Validation : tests synthétiques métier/rendu et navigateur sur fixtures publiques fictives ; confrontation locale séparée aux métadonnées publiques Zotero, Crossref et PubMed.
- Risques : texte Extra hétérogène, faux positifs sur initiales, régression des trois vues, confiance excessive dans Crossref. Conserver les détails bruts et les champs source, signaler sans corriger automatiquement. Aucun service externe nécessaire aux tests.
- Retour arrière : worktree main et branche livrée préservés ; revert du commit local, données ignorées conservées séparément.
- Revue : même session, pas de revue indépendante. Présenter un aperçu local pour la revue utilisateur avant publication.

Résultats : résumé d'archive compact et détails intacts, avertissement sensible conservé, signalement dans la qualité des noms réduits à des initiales sans permutation automatique. Les trois vues ont été inspectées en navigateur avec fixtures fictives ; aucune alerte JavaScript, aucun trafic externe dans ce test. Le filtre « A » reste fidèle à la donnée Zotero tant que celle-ci n'est pas corrigée : le signalement n'est pas présenté comme une réparation du catalogue.

Proposition privée de correction : `.local/author-correction-proposal.json` et version lisible `.md`, treize auteurs rapprochés par position/nom/initiales avec PubMed, DOI identique. Crossref reproduit l'inversion ; ne pas l'utiliser seul pour cette correction. Aucun prénom complet inventé ; la proposition de titre provient aussi de PubMed. Version Zotero observée 82 ; toute écriture future exige un GET frais et comparaison avant modification ciblée. Aucune écriture appliquée.

Conservation : empreintes des deux registres APDS lot 20 et des décisions bibliographiques antérieures revérifiées inchangées. Capture de référence à présenter : `.local/browser/table.png`, version mobile `.local/browser/mobile-list.png`. Restent revue utilisateur, application éventuelle de la correction Zotero et publication de l'interface ; ces étapes ne sont pas déduites du test local.
