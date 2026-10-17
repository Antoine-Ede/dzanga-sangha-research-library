# Correction et piste de texte intégral — 17 octobre 2026

Le catalogue contient toujours **435 références**, dans 19 collections principales ; seed 31/31, aucun titre vide ni doublon DOI ou titre sans DOI détecté par l'audit public. Aucun nouvel import dans ce lot.

## Correction appliquée

La notice MCCPAMU3, DOI 10.1111/eva.12075, inversait les champs patronyme et initiales des treize auteurs. Comparaison avec les treize auteurs dans l'ordre du [XML PubMed 24062800](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=24062800&retmode=xml), identité DOI/PMID contrôlée. Le titre a également perdu les espaces parasites « A frican » et « A nopheles ». Les initiales sont conservées, pas développées en prénoms supposés.

Sauvegarde locale de la version 82, PATCH conditionnel sur cette version, lecture après écriture et vérification publique de la version 958. Tous les champs hors créateurs, titre, provenance ajoutée et horodatage/version ont été comparés et conservés. Une seconde exécution a constaté la correction et n'a effectué aucune écriture. Rapports : [application](pinto-applied.json), [relance](pinto-rerun.json), [audit public](audit-public.json). Le script ciblé `apply_pinto_author_fix.ps1`, son XML source et les sauvegardes restent dans l'espace local de recherche ; ce bilan public n'est pas une file à rejouer.

## Texte intégral : piste, pas accès confirmé

**Constat historique du premier passage.** Le téléchargement et l'accès sont ensuite confirmés dans le [lot 011](../fulltext-2026-10-17/README.md), avec sauvegarde, correction Zotero et contrôle réel du hub. Les observations et le fichier de piste ci-dessous restent conservés pour tracer cette évolution.

Pour Flahou et al. 2014, DOI 10.1016/j.vetmic.2014.08.032, le [dépôt institutionnel UGent](https://biblio.ugent.be/publication/5794114) signale un PDF intégral de neuf pages. Son texte indexé correspond au DOI et aux méthodes utilisant des échantillons de Dzanga-Ndoki. Ce contrôle ciblé ne constitue pas une lecture des neuf pages.

Le téléchargement direct depuis cet environnement échoue par délai de connexion ; le rendu demandé au fournisseur de recherche n'a pas été obtenu. L'accès courant n'est donc pas certifié et la notice 597KZ93P reste inchangée. Le [rapport de piste](fulltext-pending.json) conserve URL et limites pour un prochain contrôle dans un navigateur. Le dépôt indique un copyright sans licence ; la possibilité de consulter n'autorise pas la republication.

Auto-revue dans la même session, pas de revue scientifique indépendante. Aucun scan APDS, original ni PDF d'éditeur ajouté à ce bilan. Après un transfert initial, le responsable précise que les registres privés APDS sont sur l'autre ordinateur et réserve finalement cet audit à l'autre session. Aucun ancien compteur ni décision n'a été réinitialisé.
