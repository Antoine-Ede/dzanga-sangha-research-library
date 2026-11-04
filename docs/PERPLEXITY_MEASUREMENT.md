# Mesure du recours à Perplexity

Ce projet ne peut pas mesurer la consommation de jetons ni le coût de Perplexity depuis le navigateur : l’interface et les fichiers reçus ne donnent ni usage facturé, ni tokens d’entrée/sortie. Une réponse de N mots ne vaut pas N tokens. En outre, aucun parcours direct équivalent n’a été exécuté en parallèle : il n’existe donc pas de baseline crédible pour chiffrer une économie.

`tools/perplexity_efficiency.py` mesure uniquement ce qui est observable localement dans le registre privé : missions, dossiers demandés, artefacts, octets, caractères, mots (séparation par espaces) et durées explicitement affichées. Les trois champs `actual_provider_tokens`, `direct_research_baseline_tokens` et `measured_token_savings` restent volontairement à `null` tant qu’une source primaire fournit ces données et qu’un protocole comparatif équivalent est lancé.

La commande locale est :

```text
python tools/perplexity_efficiency.py
```

La mesure sert à décider si les mandats restent courts et structurés. Elle ne justifie pas une affirmation d’économie de jetons, de coût ou de temps humain. Pour une comparaison future valable, il faudrait conserver avant envoi : le texte exact du mandat, sa taille, le nombre de dossiers, le résultat structuré, la durée visible, puis exécuter un échantillon comparable selon une méthode directe explicitement autorisée.
