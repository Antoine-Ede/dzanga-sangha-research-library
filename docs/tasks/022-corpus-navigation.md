# Navigation par corpus et performances

Statut : revue utilisateur acceptée le 12 novembre 2026 ; intégration et publication autorisées.

Demande : cinq onglets Publications scientifiques, Rapports techniques,
Communication, Analyse bibliographique et Guide ; qualité intégrée aux analyses.
Nom public : Dzanga Sangha Library.

Première correction locale : navigation, nom, accès qualité dans analyses,
chargement simultané des collections et références, calcul des panneaux
analytiques seulement lorsqu'ils sont ouverts. Test navigateur passé.

Analyses : page unique, histogramme empilé par type Zotero avec total annuel,
Communication comprise ; tableau accessible des valeurs ; classement des quinze
sources Communication principales ; carte schématique des pays explicitement
renseignés, liste des pays et inconnus ; qualité dans la même page.
Pays lus dans PUBLISHER-COUNTRY:code ou Publisher country:nom dans extra.
Ni langue ni suffixe du domaine ne servent de preuve. Les centres des pays et
silhouettes continentales sont approximatifs, sans frontières politiques.
Tests synthétiques et navigateur desktop/mobile passent.

Navigation finalisée le 12 novembre : rapports avec URL dédiée, remise à zéro
préservant ce corpus, retrait du type incompatible lors du changement d'onglet,
accès aux données cohérent même quand ce type manque du catalogue.
Les panneaux cachés ne sont plus reconstruits à chaque filtrage.
L'enrichissement sourcé des pays des médias reste à faire ; la carte ne prétend
pas l'avoir réalisé. Recherches nouvelles à déléguer à Perplexity selon le mandat.

Mesure publique du 12 novembre : 501 éléments de premier niveau (pas un nombre
de références bibliographiques), identités identiques dans les deux lectures.
Ancienne pagination séquentielle : 16 302 ms ; pagination par lots de trois :
10 405 ms. Gain observé de 36 %, sur un seul essai ordonné, sensible au réseau et
au cache ; ce n'est pas une promesse de durée ni le temps de rendu du navigateur.
Test reproductible : node tests/catalogue-loading.cjs --live.
Sans --live, le test est hors ligne et contrôle complétude, ordre, concurrence
maximale de trois et rejet d'un changement de version pendant la lecture.
Aucune écriture Zotero ; aucune clé utilisée.

Correction du 12 novembre après retour utilisateur : le graphique temporel
comprend exactement trois classes fixes research / communication / reports.
Les jeux de données et autres documents restent hors de leur total ; compteur
d'exclusion affiché. Tests : article et thèse regroupés, rapport et média chacun
dans leur classe, jeux de données et manuscrit exclus.

Diagnostic public de la carte : 28 notices reconnues Communication, zéro champ
PUBLISHER-COUNTRY ou Publisher country. Le fond vide n'est plus affiché :
message d'indisponibilité et classement des sources conservé. Une carte
effectivement peuplée nécessite toujours l'enrichissement sourcé des éditeurs ;
ne pas présenter ce prérequis comme terminé. Tests sans pays et avec un pays
fictif explicite ; aucune recherche documentaire ou écriture Zotero.
