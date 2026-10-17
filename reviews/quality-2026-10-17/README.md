# Revue des alertes bibliographiques — 17 octobre 2026

Le compteur public passe de **144 à 127 notices signalées**, avec les mêmes règles de contrôle et toujours **435 références**. Les 145 vues par le responsable incluaient encore le point Flahou corrigé juste avant ce lot.

| Résultat | Notices |
|---|---:|
| Alertes triées dans l'instantané initial | 144 |
| Archives APDS réservées à l'autre session, sans modification ici | 110 |
| Notices hors archives examinées ici | 34 |
| Notices corrigées dans Zotero | 23 |
| Notices désormais sans indicateur de vérification | 17 |
| Notices enrichies mais conservant une incertitude | 6 |
| Notices examinées sans correction suffisamment établie | 11 |

Les 127 restantes se composent donc des **110 archives** et de **17 notices hors archives**. Le statut de revue de chaque cas est explicite dans le [registre des décisions](decisions.json) ; les archives ne sont pas présentées comme relues scientifiquement ici. Les métadonnées de toutes les archives taguées sont identiques entre les deux instantanés publics.

## Corrections effectuées

- Quatre textes intégraux gratuits confirmés, avec téléchargement anonyme, signature PDF, empreinte et contrôle ciblé de l'identité : botanique Heimpel et al. (20 pages), évaluation UICN du TNS (26 pages), thèse de Klára Vlčková (63 pages), rapport MIKE 2005 (122 pages). Les deux derniers liens institutionnels anciens ont été remplacés par une copie universitaire précise et une copie archivée du lien CITES officiel. Le rapport de Kamiss et Turkalo (1999, 7 pages), déjà classé accessible, a également retrouvé son lien original archivé.
- Douze accès restreints documentés : achats/abonnements explicités par les éditeurs, ou emprunt contrôlé de l'édition numérisée. Les aperçus, résumés, références et fichiers de prêt chiffrés ne sont pas assimilés à un texte intégral gratuit. Cette qualification décrit les voies d'accès vérifiées ; elle ne prouve pas qu'aucune copie d'auteur gratuite n'existe ailleurs.
- Présentation des patronymes Ray et Fay corrigée après vérification : ce sont des noms réels, pas des initiales à permuter. Orthographe de Stéphane Crayne remise en casse normale. Aucune expansion de prénom supposée.
- Trois dates alignées sur les numéros de revue (Remis/Kpanou 2011, Jost Robinson/Remis 2016, Jost Robinson et al. 2017), avec dates de première mise en ligne conservées dans la provenance. Titre de revue d'Osiak corrigé en *Protetyka Stomatologiczna* depuis la fiche de son institution.

Les DOI, types, appartenances aux collections, portées scientifiques et tags existants sont conservés. Les PDF restent hébergés par leurs sources : aucun original, fichier d'éditeur ni pièce jointe n'a été republié. Le contrôle textuel ciblait l'identité bibliographique ; les couvertures des cinq PDF ont été inspectées visuellement. Aucune relecture exhaustive de leurs pages n'est revendiquée.

## Incertitudes restantes hors archives

La [liste CSV des 17 cas restants](remaining-nonarchive.csv) fournit titre, DOI le cas échéant, raison, sources consultées et champs déjà corrigés. La [revue des 34 notices](nonarchive-review.csv) conserve aussi les cas résolus. Ces tableaux sont des bilans, pas des files d'import à rejouer.

Treize notices attendent encore une confirmation de l'accès intégral ; les blocages réseau et les fiches sans fichier ne prouvent ni gratuité ni restriction. Trois thèses n'ont pas de lien public propre retrouvé (Goldsmith, Fuh Neba et Masi ; Goldsmith compte aussi parmi les accès inconnus). Le rapport annuel FTNS couvrant 2019 n'établit pas sa date de parution. L'organisme émetteur du rapport Kamiss/Turkalo n'est pas explicitement établi : les affiliations des auteurs et l'origine du questionnaire ne sont pas transformées en éditeur supposé. Ces groupes se recoupent et correspondent à 17 notices distinctes.

## Validation et reprise

Prévalidation de toutes les notices avant écriture, sauvegardes et PATCH conditionnels, comparaison des champs préservés, lectures publiques après écriture. Résultat : **23 mises à jour, zéro création, zéro échec** ; relance réelle : **zéro écriture, 23 déjà conformes**. Audit public : 19 collections, seed 31/31, aucun titre vide ou doublon DOI/titre sans DOI détecté. [Application](applied.json), [relance](rerun.json), [audit](audit-public.json), [bilan chiffré](summary.json).

Le [contrôle navigateur réel](live-quality.json) confirme 127 lignes de qualité sur 435 références, export CSV disponible et lien PDF UICN correct, sans authentification ni erreur JavaScript. Le code du site et les règles de calcul n'ont pas changé. Le contrôle commun et sa preuve de fraîcheur sont conservés localement ; tests synthétiques distincts de ces contrôles de données réelles. Auto-revue dans la même session, pas de relecteur indépendant.

Script ciblé local : `apply_quality_review_2026_10_17.ps1`, plan et journaux dans `reports/nonarchive/quality_review_2026_10_17/` de l'espace de recherche. La clé a été fournie uniquement par l'environnement du processus et retirée ensuite ; aucune clé dans ce bilan. Pour revenir sur une correction, comparer d'abord la notice actuelle à sa sauvegarde et restaurer uniquement les champs visés, sans écraser d'enrichissement ultérieur. L'audit APDS continuera sur l'autre ordinateur/session conformément à la décision du responsable.
