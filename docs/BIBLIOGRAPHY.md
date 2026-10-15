# File bibliographique locale

Ce prototype prépare une revue : il n'importe rien dans Zotero. Le site continue de lire Zotero. Les sorties contiennent des propositions, des preuves et des décisions locales, jamais une certification scientifique ou une autorisation de diffuser les documents.

## Essai sans réseau, clé ou fournisseur d'IA

Depuis la racine du worktree, sous PowerShell :

```powershell
.\dev.ps1 bibliography --db tutorial.sqlite ingest tests/fixtures/candidates.json
.\dev.ps1 bibliography --db tutorial.sqlite ingest tests/fixtures/candidates.json
.\dev.ps1 bibliography --db tutorial.sqlite catalogue-file tests/fixtures/catalogue.json --as-of 2026-10-15 --label 'Jeu fictif de test'
.\dev.ps1 bibliography --db tutorial.sqlite export --out tutorial-review-1.json
.\dev.ps1 bibliography --db tutorial.sqlite status
```

Les quatre observations fictives donnent trois candidats, même après relance. Les deux sources d'un même DOI sont regroupées avec leurs dates contradictoires. Un rapport sans auteur, date ni DOI reste présent. Un titre ressemblant ne provoque aucune fusion. Les fichiers sont dans `.local/`, ignoré par Git. Choisir d'autres noms si ces sorties existent déjà : un export n'écrase pas une ancienne revue.

Sur les autres systèmes, remplacer `.\dev.ps1 bibliography` par `python tools/bibliography.py` avec Python 3.11+. Aucune dépendance à installer pour cette CLI.

## Lire puis décider

Ouvrir le JSON exporté comme texte. Pour chaque candidat :

- `metadata` est la première valeur disponible pour faciliter la lecture, pas une valeur arbitrée ; examiner `field_proposals`, leurs `evidence_refs`, `conflicts` et `missing_metadata`.
- `observations` conserve source, URL, identifiant externe, métadonnées fournies, avertissements, extraits et localisateurs ; `discoveries` conserve requêtes et premières/dernières récupérations.
- `relevance_proposal` reste distinct de `human_decision`. Par défaut, le moteur s'abstient : la mention du lieu ne prouve pas des travaux APDS. L'absence de DOI n'est pas une erreur.
- `possible_catalogue_duplicates` et `possible_queue_duplicates` sont des pistes. L'indicateur de ressemblance du titre n'est pas une probabilité scientifique. Examiner DOI, auteurs, date, édition et source avant toute décision.
- `catalogue_snapshot` donne provenance et fraîcheur du catalogue comparé. Sans instantané, le rapprochement est incomplet. `content_dissemination: not_assessed` reste vrai même après une décision de conservation.

Recopier l'identifiant `cand-...` exact de l'export dans une décision explicite :

```powershell
.\dev.ps1 bibliography --db tutorial.sqlite decide ID_CANDIDAT --decision defer --reviewer 'Relecteur du test' --reason 'Vérifier la date dans une source indépendante'
.\dev.ps1 bibliography --db tutorial.sqlite export --out tutorial-review-2.json
```

Choix : `retain` (conserver pour la suite), `reject` ou `defer`. Aucun ne crée une référence validée ni une écriture distante. L'identité du relecteur est déclarative, sans authentification. Ne pas enregistrer une décision humaine pour le compte de quelqu'un qui ne l'a pas prise.

La portée reste `indeterminate` tant que les éléments sont insuffisants. Pour `--scope DSPA-Core` ou `DSPA-Relevant`, fournir aussi `--evidence-id OBSERVATION`, `--scope-basis JUSTIFICATION` et `--scope-quote EXTRAIT_EXACT`. L'extrait doit provenir des éléments sources, au-delà du seul titre. Pour Core, la justification doit établir des données, observations, échantillons ou travaux provenant des APDS. Les contrôles de forme n'évaluent pas cette vérité : le relecteur doit vérifier l'origine. Une synthèse de gestion pertinente sans données APDS peut relever de Relevant.

Les décisions sont ajoutées à un historique et conservées aux relances. De nouvelles observations ou un catalogue dont l'empreinte change donnent `needs_recheck`, sans effacer la dernière décision. Les corrections tardives de DOI conservent l'identifiant local ; un conflit d'identité entre candidats demande une réconciliation manuelle, sans fusion automatique de leurs historiques.

## Recherche publique bornée, facultative

Utiliser une base séparée du jeu fictif :

```powershell
.\dev.ps1 bibliography --db public.sqlite catalogue --pages 6
.\dev.ps1 bibliography --db public.sqlite discover --query 'Dzanga-Sangha' --pages 1 --rows 5
.\dev.ps1 bibliography --db public.sqlite export --out public-review-1.json
```

Ces commandes font uniquement des GET HTTPS aux API publiques de Zotero (groupe 6701789) et Crossref. Elles n'envoient ni PDF, ni inventaire local, ni décision, ni clé. Crossref reçoit la requête, le curseur et la taille de page ; Zotero reçoit le groupe et les paramètres de pagination. N'utiliser que des requêtes publiques. Aucun abonnement ni service payant n'est utilisé. Les URLs de documents présentes dans les métadonnées ne sont pas téléchargées.

La recherche porte par défaut sur le titre. `--search-field bibliographic` permet une recherche plus large, souvent plus bruitée. Le petit essai réel a montré des résultats sans rapport apparent en mode large : la découverte n'établit jamais la pertinence. Crossref ne couvre pas toutes les thèses, archives, données et publications sans DOI ; l'entrée JSON publique permet de préparer ces cas, sans prétendre les découvrir automatiquement.

`--pages` limite le travail de chaque invocation. Relancer la même requête, taille de page et champ reprend le curseur enregistré. Un run terminé ne recharge rien ; `--restart` recommence sa pagination sans supprimer candidats ou décisions. Pour actualiser un catalogue terminé, utiliser `catalogue --restart`. Seul un instantané complet d'une même version Zotero remplace le précédent ; un changement de version en cours exige un redémarrage. Ne pas présenter un instantané incomplet comme un catalogue actuel.

Délais : 20 secondes par requête, trois tentatives au maximum pour les erreurs transitoires, réponses limitées à 8 Mo, redirections refusées. Les pages acceptées et curseurs sont enregistrés dans une transaction. Une page invalide ne fait pas perdre les précédentes. Les pauses serveur sont persistées dans le run et respectées même avec `--restart`. Attendre l'échéance indiquée avant de reprendre ; ne pas lancer des bases ou requêtes parallèles pour contourner une pause. Les curseurs peuvent expirer : redémarrer la requête après examen, sans réinitialiser la base.

## Métadonnées publiques et IA facultative

Le format d'entrée est une liste d'observations, illustrée par `tests/fixtures/candidates.json` : `visibility` explicite (`public_metadata` ou `synthetic`), `source`, `record_id` stable, `url`, `query`, `retrieved_at` avec fuseau, `metadata` et `evidence` avec champ/texte/localisateur. Les noms d'auteurs ne doivent pas être déduits de signataires ou de participants. Les dates et types d'événements incertains restent dans les preuves, sans invention de date de publication.

La déclaration `public_metadata` ne déclassifie pas une donnée privée : vérifier son contenu avant ingestion. Aucun original, OCR sensible, journal privé, carte sensible ou secret ne doit entrer dans ces fichiers, même comme exemple. Les conventions APDS (original sous accès encadré, transcription, copie expurgée, notice) restent distinctes et ne sont pas remplacées par ce format de propositions.

Le fournisseur `deterministic` fonctionne hors ligne. `export --provider simulated` exerce un contrat de sortie : statut proposition, incertitudes, abstention et références vérifiables aux extraits. Il ne fait aucun appel d'IA. Une sortie valide ne prouve pas l'exactitude des enrichissements. Pydantic AI et Spec Kit ont été évalués dans `DECISIONS.md` ; aucune de ces dépendances n'est nécessaire au parcours actuel. Ajouter un fournisseur réel demanderait un besoin démontré et un accord explicite sur données transmises et coûts.

## Sauvegarder, contrôler et reprendre

```powershell
.\dev.ps1 bibliography --db tutorial.sqlite backup --out tutorial-backup.sqlite
.\dev.ps1 check
.\dev.ps1 check --verify-proof
```

La sauvegarde SQLite est contrôlée par `integrity_check` et refuse une destination existante. Pour éprouver une restauration, utiliser `--db tutorial-backup.sqlite status` ; conserver l'original et donner un nouveau nom à toute copie de travail. Un export JSON est une preuve de revue, pas une sauvegarde complète des curseurs ni un format d'import Zotero.

La preuve commune `.local/verification.json` identifie le code testé, pas les bases ignorées. Un essai réel a une preuve distincte (`.local/public-smoke-report.json` pour le lot initial), avec SHA du code, empreinte de la base et des exports, paramètres et limites. Les données locales doivent être sauvegardées séparément avant de supprimer un worktree. Un retour au checkout initial ou un revert local du lot n'efface pas ces données.
