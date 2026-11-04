# Plan d’import Communication vérifié délégué

Ce lot propose 33 notices `webpage` issues de la revue Communication : 32 entrées `verified_delegated` du TSV final et SUP-51, confirmé dans la revue prioritaire. L’import reste séparé de la réception Perplexity et emploie un contrôle live URL/titre avant chaque création.

## Exclusions volontaires

- SUP-47 : hors périmètre selon décision utilisateur du 4 novembre ; la source concerne le Gabon et n’établit pas un lien APDS.
- SUP-16 : index d’auteur évolutif, pas une œuvre individuelle.
- SUP-32 : deux pages institutionnelles contextuelles évolutives, pas une œuvre individuelle.
- SUP-35 : fiche de projet régionale non datée, pas une œuvre individuelle.
- Tous les statuts `partial` ou `blocked` restent hors import.

Le manifeste [communication-import-candidates.json](communication-import-candidates.json) conserve les titres, créateurs seulement lorsqu’un rôle compatible est explicite, dates prudentes, URL, tags contrôlés et limitations. Les rôles plus complexes restent dans `extra` au lieu d’être transformés en auteurs.

## Exécution autorisée

`import_verified_communication.ps1` s’exécute d’abord en prélecture puis, seulement avec `-Apply`, crée les notices absentes dans le groupe 6701789. Il contrôle les droits de la clé, l’identifiant de groupe, le manifeste, les doublons URL/titre, les réponses batch et chaque création. Il ne supprime, ne met à jour ni ne déplace aucune notice existante.

Le nombre final de créations n’est pas présumé : l’instantané local du 24 octobre signalait déjà trois correspondances, mais la déduplication live fait autorité. Les tags `EVIDENCE:Perplexity-Delegated` et les limites dans `extra` empêchent de présenter cette importation comme une relecture primaire indépendante par Codex.
