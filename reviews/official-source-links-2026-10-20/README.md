# Liens des sources officielles — 20 octobre 2026

Demande : proposer le lien du dépôt officiel même lorsque le texte intégral n'est pas confirmé. **Six URL corrigées dans Zotero : une notice HAL et cinq pages éditeur.** DOI, titres, auteurs, dates, collections et tags d'accès conservés. Aucune création ni copie PDF publiée.

- [Diallo — notice HAL](https://riip.hal.science/pasteur-00540435v1) : identité confirmée par le DOI exact dans l'API HAL ; aucun fichier principal déclaré. C'est une notice bibliographique, pas un PDF gratuit vérifié.
- [Night and day](https://onlinelibrary.wiley.com/doi/10.1111/aje.12344), [BaAka women's health](https://onlinelibrary.wiley.com/doi/10.1002/ajhb.22817), [Primate and ungulate abundance](https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2028.2010.01229.x), [Comparative ecology of two African forest mongooses](https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2028.1997.086-89086.x) et [Censusing rainforest game species](https://onlinelibrary.wiley.com/doi/10.1046/j.1365-2028.1999.00154.x) : adresses primaires déposées par l'éditeur dans Crossref pour les DOI correspondants. Leur présence n'établit pas l'accès gratuit au texte intégral.

Le contrôle du hub public a mis au jour une omission : la vue Tableau affichait les PDF mais masquait les autres URL complémentaires. La correction proposée affiche la même source dans Tableau, Cartes et Liste compacte : **Notice HAL**, **Source en ligne**, ou **Consulter le PDF** lorsque l'URL est celle d'un PDF. Suite à la précision du responsable le 22 octobre, le **titre ouvre désormais le PDF en priorité**, puis l'URL du document, puis le DOI vers la page officielle en recours ; une notice HAL/PubMed reste complémentaire si un DOI existe. **Notice Zotero** reste un lien distinct. Le lien complémentaire refuse les URL contenant des identifiants et les protocoles non web.

Cette priorité PDF utilise l'URL HTTP(S) déjà renseignée dans Zotero dont le chemin se termine en `.pdf`, paramètres acceptés. Elle couvre notamment les six copies publiques du projet. Ensuite, l'URL du document est préférée au DOI : cela ouvre aussi une route de téléchargement PDF sans suffixe `.pdf`. Une notice HAL ou PubMed reste complémentaire si le DOI fournit la destination de publication. Le DOI sert sinon de recours. Aucun fichier Windows privé publié ni pièce jointe découverte automatiquement. Le comportement est testé avec une notice fictive possédant à la fois un DOI et un PDF, en ouvrant son titre au clavier dans les trois vues.

## Résultat bibliographique

435 références, 19 collections, seed 31/31, gouvernance et Harris conformes, aucun titre vide ou doublon détecté. **122 notices signalées**, dont 110 archives réservées à l'autre session et [12 cas hors archives toujours incertains](../historical-access-2026-10-20/remaining-nonarchive.csv). Ajouter une adresse officielle ne tranche pas leur accès ; les règles et le compteur sont inchangés.

Six sauvegardes avant PATCH conditionnels, lectures publiques conformes et relance : zéro écriture, six déjà conformes. Comparaison intégrale des données des notices entre les instantanés : seuls URL et Extra des six cibles ont changé, outre leurs versions et dates de modification ; tags et toutes les autres notices identiques. Aucun fichier original consulté ou redistribué dans ce lot.

## Preuves et limites

- [Bilan chiffré](summary.json), [six décisions et versions](decisions.json), [métadonnées des sources](primary-proofs.json), [liens CSV](official-links.csv).
- [Application](applied.json), [relance](rerun.json), [audit public](audit-public.json).
- Les sources démontrent l'identité des liens, pas une lecture scientifique des articles. Les blocages techniques ne sont pas des restrictions attestées. Semantic Scholar signale Diallo Bronze ; ce signal n'est pas converti en accès gratuit vérifié.
- Auto-revue dans la même session. La modification d'affichage nécessite une revue utilisateur avant fusion, selon AGENTS.md. Les scripts ciblés et sauvegardes sont privés ; ne pas rejouer les imports historiques.
- Contrôle commun réussi : syntaxe JavaScript, tests Python, rendu synthétique et navigateur sans trafic externe. Ouverture clavier des sources dans les trois vues, liens DOI/PDF/Zotero préservés, mobile contrôlé. Aperçu local sur données publiques Zotero : lien HAL exact visible dans le tableau ; capture privée conservée pour la revue utilisateur. Le correctif d'interface n'est pas encore publié sur Pages.

Retour arrière : restaurer sélectivement URL/Extra depuis les sauvegardes après inspection des versions actuelles. La partie interface peut être annulée séparément. Révoquer la clé temporaire après les opérations authentifiées des deux sessions.
