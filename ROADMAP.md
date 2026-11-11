# Feuille de route active — Dzanga-Sangha Research Library

Dernière consolidation : **11 novembre 2026**. Les détails, preuves et
compteurs historiques sont conservés dans [STATE.md](docs/STATE.md) et les
fiches de lots dans [docs/tasks](docs/tasks/). Cette feuille ne remplace pas
ces traces ; elle indique ce qui mérite une décision ou un travail ultérieur.

## État de référence

- `main` est le point de reprise du hub et du code. GitHub Pages publie depuis
  cette branche ; le hub public est disponible.
- La structure Zotero validée comprend 19 collections de premier niveau, une
  seule collection `00 - A verifier`, une note de gouvernance et le livre de
  Harris. Le dernier audit bibliographique complet documenté a contrôlé le
  seed, les doublons DOI et les titres vides ; consulter STATE pour ses limites
  et son horodatage.
- Le corpus Communication préparé à partir de la livraison déléguée compte 33
  œuvres individuelles : la prélecture finale du responsable les a toutes
  reconnues dans Zotero (30 créations et 3 notices déjà présentes). Ce résultat
  ne transforme pas les autres pistes Communication en sources validées.
- Les jeux de données et les notices scientifiques déjà intégrés restent soumis
  aux règles de portée DSPA-Core/DSPA-Relevant, de provenance et d’accès.
- L’audit des archives APDS est maintenu **hors de ce checkout**, sur l’autre
  ordinateur et dans l’autre session. Ne pas recopier ses fichiers privés, ses
  compteurs ou ses scans ici.

## Priorités actives

### 1. Branche de guide examinée, à archiver ultérieurement

`feat/library-guide` (`f04245a`, worktree `hub-publication`) a été comparée à
`main` le 11 novembre. Son guide est déjà couvert, et enrichi, par le mode
d’emploi publié : ouverture des PDF publics, onglet Communication et règles de
contribution actuelles. Une fusion créerait des conflits dans `.gitignore`,
`app.js`, `index.html` et `styles.css` sans apporter de contenu utile. Ne pas
créer de PR ni fusionner cette branche ; la conserver jusqu’à confirmation que
plus aucune session ne dépend de son worktree, puis l’archiver de manière
récupérable.

### 2. Revue humaine des découvertes bibliographiques

Conserver une séparation stricte entre :

- références scientifiques ;
- rapports de gestion ou de développement communautaire ;
- jeux de données ;
- contenus Communication.

Les candidats issus d’OpenAlex et des recherches complémentaires restent une
file de revue, pas un corpus à importer. Avant toute création Zotero : confirmer
l’identité, le DOI ou l’identifiant, la portée géographique, la classification
DSPA et la collection cible ; dédupliquer contre le groupe en direct. Une
mention de Dzanga-Sangha, de Shelly Masi, Klára Petrželková ou Lara Nellissen ne
suffit pas à déclarer une source DSPA-Core.

Le bilan local historique du 5 octobre, conservé dans l’autre copie de travail,
atteste un tri déterministe de 1 207 candidats : 347 retenus pour revue, 594
exclus et des relations d’alias, de composant ou de version documentées. Il ne
constitue ni une vérification actuelle du groupe Zotero ni une autorisation
d’import. Un seul cas reste en attente de source : l’abstract individuel AAPA
2014 « Women, worms and work » (`10.1002/ajpa/22488`). Le DOI identifie les
proceedings, pas nécessairement cet abstract ; conserver ce cas sans création
Zotero jusqu’à obtention d’une source primaire ou d’une bibliographie d’auteur
faisant autorité.

### 3. Terminer les cas Communication partiels ou bloqués à la demande

La livraison Perplexity est préservée dans
`reviews/communication-supplement-2026-10-25/`. Les statuts délégués, les
limites et la décision d’exclusion SUP-47 doivent rester visibles. Toute
nouvelle recherche web sur ces cas passe par Perplexity Recherche standard ; ne
pas traiter les résultats comme une validation primaire automatique ni publier
de contenu protégé.

### 4. Maintenir le hub public

Préserver recherche, tableau par défaut, vues alternatives, filtres,
accessibilité, export CSV, onglets Analyse, Qualité, Communication et Aide.
Tout changement d’interface doit avoir un contrôle syntaxique, un test local et
une revue utilisateur avant fusion/publication. Le groupe Zotero public demeure
la source de vérité ; aucune clé ne doit apparaître dans le site.

### 5. Reprendre séparément les archives APDS

La prochaine reprise APDS se fait seulement depuis les registres privés de
l’autre ordinateur. Appliquer la décision D005 : tri proportionné, contrôle
ciblé des alertes et séparation entre original, notice, OCR et copie expurgée.
Une notice publique ne donne jamais l’autorisation de diffuser un PDF.

## Veille bibliographique

La veille mensuelle est actuellement **en pause à la demande du responsable**.
Lors de sa réactivation, elle doit seulement produire un fichier local de revue
daté avec les sources, raisons de pertinence, décisions proposées et doublons
possibles. Elle ne doit ni importer dans Zotero, ni publier des archives, ni
utiliser ou demander de secret.

## Entretien Git

- Aucune pull request n’est ouverte au moment de cette consolidation.
- Les worktrees `library-guide-current` et `research-closeout` pointent vers
  des branches déjà fusionnées ; les conserver tant qu’une autre session peut
  en avoir besoin, puis les archiver de manière récupérable.
- Les branches historiques fusionnées peuvent être nettoyées après vérification
  qu’aucune preuve privée ou travail parallèle n’en dépend.
- Les imports Zotero doivent toujours être précédés d’une prélecture, d’un
  contrôle de version et d’une sauvegarde avant toute mise à jour ou suppression.

## Prochain petit pas recommandé

Choisir un petit lot de candidats bibliographiques à revue humaine, en gardant
les rapports, les données et les contenus Communication séparés. Conserver la
clé API temporaire révoquée ou la révoquer dès qu’aucune écriture authentifiée
n’est nécessaire.
