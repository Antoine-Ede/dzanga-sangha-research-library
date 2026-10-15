# Suivi du projet et reprise de l’audit APDS

## Priorité actuelle — système local de développement et propositions

Mission du 15 octobre : [socle de développement](docs/tasks/001-development.md), puis [file bibliographique locale](docs/tasks/002-bibliography.md). État effectivement vérifié et prochaine étape : [STATE](docs/STATE.md). Aucun import, push, déploiement ou merge n’appartient à cette mission. Valider le parcours manuel avant toute IA réelle ou automatisation.

## Bilan historique APDS conservé

État consigné le **15 octobre 2026** ; dernier contrôle documentaire détaillé : **14 octobre 2026, lot 19**. Ce document clôt le lot de travail `feature/apds-archive-catalogue` et prépare sa reprise après l’amélioration du développement souhaitée par le responsable du projet. **L’audit exhaustif des archives n’est pas terminé.**

## Travail livré

- **118 nouvelles notices Zotero** importées en deux passes (82 puis 36), dans les collections existantes. Elles indiquent la conservation d’une copie à la Bibliothèque des APDS et leur identifiant d’inventaire. Les fichiers d’import du [catalogue](catalogue/apds-2026-10-08/README.md) sont une trace historique, pas une file à réimporter.
- Les documents pertinents ont une notice même lorsque des informations manquent ; les incertitudes restent explicites. Vingt-cinq originaux sensibles de la seconde passe sont représentés par des métadonnées minimales et un avertissement de consultation encadrée.
- **Six plans historiques expurgés, 83 pages publiques**, avec présentation, provenance et empreintes dans le [manifeste](catalogue/apds-2026-10-08/plans-publics/manifest.json). Les diagnostics, bilans et propositions historiques sont conservés avec leur attribution. La copie de Yandoumbé a été renforcée le 13 octobre ; les six copies ont été recontrôlées au fil des derniers lots.
- Affichage de la provenance, des lacunes et des avertissements de consultation dans les cartes, la liste et le tableau de la bibliothèque.
- **13 notices existantes enrichies et vérifiées après rechargement** pendant la revue OCR : quatre pour la préférence de source en ligne/provenance et neuf pour les lacunes, limites ou plans. Ce ne sont pas 13 nouveaux imports. Les autres propositions de métadonnées ne sont pas toutes appliquées.
- Les évolutions indépendantes déjà présentes sur `main` (catégories, analyses et qualité bibliographique) sont conservées lors de l’intégration.

## Couverture réelle du contrôle

Les chiffres portent sur les **fichiers scannés**, variantes comprises, et sur leurs pages PDF, pas sur un nombre de publications uniques.

| Indicateur au point d’arrêt | Réalisé | Reste / limite |
| --- | ---: | --- |
| Inventaire local | 170 PDF, 6 012 pages | L’intégralité des originaux physiques n’est pas certifiée |
| Transcriptions préparées en Markdown privé | 170 | Une conversion ne constitue pas une relecture |
| Revue OCR détaillée, page par page | 41 scans, 556 pages | 129 scans, 5 456 pages à examiner dans ce suivi |
| Lecture OCR suffisamment reconnue | 327 pages | 229 pages examinées nécessitent les images ou ont un OCR insuffisant ; certaines sont blanches |
| Contrôle visuel cumulé | 52 fichiers dont toutes les pages ont été ouvertes ; 791 pages | 5 221 pages restent à contrôler visuellement |
| Lisibilité des pages visuellement examinées | 733 pages contrôlées lisibles | 58 pages partiellement illisibles, sans certification de lecture intégrale |
| Regroupement des 41 scans relus | 36 dossiers bibliographiques | 3 guides généraux hors périmètre ; 33 dossiers concernent le catalogue |

Les contrôles OCR et visuels **se recoupent et ne doivent pas être additionnés**. Certaines variantes ont été relues sans que toutes les autres copies d’une même publication aient été comparées. Un scan ouvert n’est pas nécessairement lisible ni complet.

## Prochaines étapes

1. **Mettre en place puis éprouver l’amélioration du développement** : périmètre désormais précisé dans les deux fiches ci-dessus ; résultats dans STATE. Conserver une procédure de validation avant publication et distinguer les changements Git des écritures dans Zotero, qui alimentent immédiatement le site public.
2. **Reprendre la revue documentaire depuis les registres privés**, sans réinitialiser les compteurs : examiner les 129 scans restants dans le suivi OCR et les 5 221 pages encore en attente dans le suivi visuel. Revenir aux images pour les tableaux, cartes, annotations et passages mal reconnus ; conserver les limites lorsqu’un original reste illisible.
3. **Comparer les propositions restantes aux notices Zotero actuelles**, puis appliquer uniquement les compléments validés, sans écraser les enrichissements indépendants. Le lot de propositions de 36 dossiers est partiellement appliqué ; les 13 notices déjà enrichies ne signifient pas que tous leurs champs proposés ont été réconciliés. Vérifier la sauvegarde après rechargement et consigner les champs effectivement modifiés.
4. **Poursuivre la recherche des versions en ligne identiques** : vérifier titre, auteurs, date, édition/langue et pagination ; privilégier le DOI confirmé ou le dépôt institutionnel. Conserver la provenance APDS et les lacunes du scan. La référence citée dans un rapport, sa traduction ou un article ultérieur ne lui donnent pas leur DOI. Certains liens institutionnels ont été confirmés sans audit visuel du volume en ligne entier ; le lien direct vers l’édition française d’un chapitre reste à confirmer.
5. **Compléter les comparaisons de variantes et rechercher les pages manquantes**. Des scans préférables ont été identifiés, mais l’équivalence de toutes les copies et l’intégralité des originaux ne sont pas établies. Ne pas inventer les dates de rédaction à partir des périodes de terrain, ni les auteurs à partir des signataires.
6. **Préparer les autres copies publiques pertinentes**, après examen des droits et, lorsque nécessaire, expurgation ciblée. Plusieurs documents relus pourraient être diffusés ; leurs copies finales n’ont pas été produites. Les détails des retraits restent dans l’audit privé. Contrôler toutes les pages du PDF produit, sa lisibilité, son empreinte et l’absence de texte source récupérable, annotations ou pièces jointes avant diffusion.
7. **Vérifier la cohérence des indicateurs de qualité avec les notices d’archives**. Le contrôle actuel de qualité reconnaît les tags d’accès `Open` et `Restricted` ; `Restricted-Original` peut encore déclencher « Accès à déterminer ». Distinguer accès à l’original et disponibilité d’une copie expurgée dans le prochain chantier, sans transformer l’avertissement en autorisation de diffusion.
8. **Suivre les anciennes versions publiques** : la révision d’une copie et la mise à jour du lien préféré dans Zotero ne retirent pas ses versions antérieures de l’historique Git ou de leurs URL immuables. Évaluer séparément le besoin de retrait de l’ancienne révision de Yandoumbé ; aucune purge d’historique ni suppression des copies distantes n’a été réalisée.

## Conditions à conserver lors de la reprise

Une notice bibliographique publique ne vaut pas autorisation de publier son PDF. La présence en ligne ne règle pas les droits de redistribution. Conserver les originaux sensibles sous consultation encadrée ; ne pas publier le corpus OCR privé, les inventaires avec chemins locaux, les constatations personnelles ou les cartes détaillées non validées. Les propositions d’un plan ancien ne prouvent pas leur mise en œuvre et ses diagnostics ne décrivent pas automatiquement la situation actuelle.

Les fichiers JSON de ce dépôt sont des **instantanés d’import d’octobre**, pas une sauvegarde exhaustive à jour du groupe Zotero. Les enrichissements ultérieurs sont tracés dans les journaux locaux. Avant tout import, comparer clés Zotero, DOI et identité bibliographique pour éviter les doublons.

## Point de reprise local — hors dépôt public

Les fichiers suivants sont conservés dans l’espace de travail local, à côté du checkout `work/dzanga-sangha-research-library`. Ils ne sont pas inclus dans le dépôt et doivent être sauvegardés séparément avant migration ou nettoyage de cet espace :

- Inventaire et contrôle final du lot 19 : `outputs/inventaire-prive-apds-final.json`, `outputs/verification-revue-ocr-2026-10-14-lot19.json`.
- Compteurs et bilan : `outputs/revue-ocr-progress.json`, `outputs/controle-visuel-progress.json`, `outputs/bilan-revue-ocr.md`.
- Décisions par page et états de reprise : `outputs/revue-ocr-prive.*`, `outputs/controle-visuel-prive.*`, `work/text-audit/`, `work/visual-audit/`, `work/review-text/`.
- Propositions et écritures Zotero : `outputs/enrichissements-notices-revue-ocr.json`, `work/zotero-online-preference-applied.json`, `work/zotero-ocr-notes-applied.json`, avec les preuves locales de vérification.

Ces dossiers privés permettent de reprendre l’analyse ; ils ne doivent pas être téléversés en bloc dans GitHub ou Zotero. La fusion clôt la branche de ce lot, pas les tâches ouvertes de cette feuille de route.
