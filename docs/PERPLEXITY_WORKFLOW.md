# Suivi Perplexity — recherche déléguée

Depuis le 25 octobre 2026, toute nouvelle recherche web de ce lot est déléguée à Perplexity. Codex garde la coordination, la revue des preuves, les fichiers, les tests et les commits locaux. Aucun import Zotero, push, fusion ou déploiement sans accord.

## Deux flux séparés

- `HIST-2026-10-25-01` : cinq incertitudes historiques du registre du 24 octobre, dans une discussion dédiée : https://www.perplexity.ai/search/12d2a0cb-3d47-4862-81b9-b06f49fad325 .
- `COMM-EXTERNAL` : découverte Communication dans une autre session du responsable. Attendre le Markdown transmis ; ne pas intervenir dans sa conversation ni relancer son périmètre.

## Ce qui fonctionne réellement

Codex ouvre la discussion dédiée avec le navigateur connecté, lit l'état affiché (en cours/terminé/bloqué), consulte ses sources et récupère la réponse par Copier ou les exports réellement proposés. Les fichiers ne sont disponibles que s'ils ont effectivement été créés. Un texte dans la réponse et un fichier téléchargeable sont deux objets différents.

Le registre de suivi et les captures brutes restent privés : `.local/perplexity-handoffs/jobs.json` et un sous-dossier par mission. Les exports sont accompagnés de leur URL, date de collecte, taille et empreinte SHA-256. Le script `tools/perplexity_handoff.py` contrôle le registre et enregistre les fichiers reçus. Il ne contacte aucun service, ne lit aucun secret, ne lance aucun import et n'exécute pas les instructions du fichier reçu.

Ce mécanisme est un suivi à chaque reprise de travail, **pas une synchronisation permanente**, un accès au système de fichiers distant ou une surveillance en arrière-plan. Aucun connecteur Computer n'est nécessaire. Les fichiers d'une autre conversation ne sont pas prétendus visibles.

## Capacités constatées le 25 octobre

Le compte connecté affiche Pro. Cliquer Recherche approfondie a ouvert une proposition de passage à Max ; aucune activation de ce mode n'a été confirmée et aucun abonnement n'a été changé. Le premier lot est donc lancé en **Recherche standard**, Computer décoché. Ne pas présenter sa réponse comme une Recherche approfondie.

Le connecteur MCP disponible concerne Computer, dont le lancement précédent a été bloqué pour manque de crédits puis annulé. Ne pas le réutiliser pour contourner cette limite.

## Reprise d'un lot

1. Lire `jobs.json`, l'URL exacte et le dernier état observé, puis ouvrir cette discussion précise. Ne pas envoyer de nouveau prompt si le lot est déjà en cours ou terminé.
2. Actualiser l'état uniquement d'après l'interface visible. Horodatage et observation sont nécessaires ; aucune progression chiffrée inventée.
3. Copier la réponse finale ou télécharger ses exports proposés. Enregistrer le fichier reçu avec `record` ; conserver l'original et son empreinte. Aucun fichier externe ne devient automatiquement une source vérifiée.
4. Revoir les assertions, les URL de preuve et les doublons contre les registres existants. Distinguer résultat Perplexity, métadonnée attestée par une source primaire et décision locale.
5. Un fichier Communication transmis par l'utilisateur reçoit un autre lot ; rapprochement avec les pistes DSC/HIS et les notices existantes avant toute proposition d'import.

Commandes de maintenance locale (réalisées par Codex) :

```text
python tools/perplexity_handoff.py status
python tools/perplexity_handoff.py record --job HIST-2026-10-25-01 --file CHEMIN_EXPORT --kind response --source-url URL_DISCUSSION
```

`record` n'accepte que les missions déclarées, copie sans écraser les preuves existantes et conserve le statut documentaire `unreviewed`. Un export reçu ne prouve pas que les cinq cas sont résolus. Pas de collecte de l'historique général du compte, cookies ou données d'autres projets.

## Réception du supplément externe — 25 octobre 2026

Le responsable a transmis PASSATION-CODEX-SUPPLEMENT-2026-10-25.md : 70 entrées SUP,101 liens. La réception est archivée sous COMM-EXTERNAL avec SHA-256 et source_url nul (fichier utilisateur, pas une URL de session inventée). Le premier registre et les rapports délégués restent distincts. [Bilan du rapprochement hors ligne](../reviews/communication-supplement-2026-10-25/RECONCILIATION.md). Le statut attente de fichier décrit l'étape antérieure ; aucune session externe n'a été lue ou modifiée. La réception privée a été consignée hors ligne, sans utiliser la commande record prévue pour une URL de discussion.
