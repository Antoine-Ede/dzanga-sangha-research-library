# Revue PubMed du 16 octobre 2026

Ce dossier consigne les dix décisions restant ouvertes dans la recherche du 14 octobre. Il s'agit d'une revue par l'assistant, dans la même session, avec import autorisé par le responsable ; aucune revue scientifique indépendante ou décision humaine article par article n'est revendiquée.

La recherche initiale avait reçu 84 résultats : 62 déjà rapprochés du catalogue et 22 à examiner. Les cinq premières acceptations et le rapport FTNS ont été importés entre-temps et sont présents au contrôle de reprise. Les dix derniers candidats donnent **8 acceptations et 2 exclusions**. Bilan des 22 : **13 acceptations, 7 exclusions, 2 corrections associées**, aucune décision laissée vide. Ce bilan ne couvre pas exhaustivement PubMed ni les autres moteurs.

## Décisions et preuves

`decisions.json` conserve identifiants, sources, localisateurs, justification et limites. `accepted.csv` est le manifeste historique de ce lot, **pas une nouvelle file à réimporter**. Rechercher d'abord les DOI dans Zotero ; les scripts de recherche restent dans l'espace local privé. Les métadonnées publiques et décisions sont conservées ici, aucun PDF d'éditeur ni clé d'API.

| PMID | Référence abrégée | Décision | Preuve décisive |
| --- | --- | --- | --- |
| 40915313 | Malaka et al., mpox, 2025 | Relevant | Résultats du Lancet Microbe : district de Sangha-Mbaéré explicitement inclus ; provenance APDS précise non établie. |
| 33711161 | Amin et al., pangolin, 2021 | Core | Original déposé par l'auteur : collecte et localité type APDS. |
| 29475742 | D'Amico et al., Ixodes rasus, 2018 | Core | Introduction originale de l'éditeur : spécimens de Dzanga-Ndoki. |
| 29205130 | Vlčková et al., stress et microbiome, 2018 | Core | PDF institutionnel, p. 2 : groupes de Bai Hokou et Mongambe. |
| 27440885 | Madinda et al., polyomavirus, 2016 | Core | Tableau 1 du PDF original : 23 échantillons APDS, aucun positif dans cette ligne. |
| 26923597 | Gomez et al., microbiome BaAka/Bantu, 2016 | Core | Méthodes de l'original déposé par l'auteur : échantillons de 28 BaAka et 29 Bantu des APDS. |
| 25862141 | Hoppe et al., adénovirus, 2015 | Core | Tableau 1 original : chimpanzés, gorilles et humains des APDS. |
| 25248691 | Flahou et al., Helicobacter, 2014 | Core | Échantillonnage original de l'éditeur : gorilles habitués et non habitués de Dzanga-Ndoki. |
| 38849672 | Gogarten et al., prévention, 2024 | Écarté de cette sélection | Perspective générale ; pas d'application spécifique APDS établie dans les éléments examinés. |
| 34599175 | SARS-CoV-2 B.1.620, 2021 | Écarté de cette sélection | Analyses nationales et voyages ; pas de lieu APDS ni de lien de gestion assez direct établi. |

Les méthodes, tableaux et passages géographiques sont ciblés. Trois pages d'originaux téléchargés ont été contrôlées aussi en image ; aucune lecture visuelle exhaustive des volumes n'est affirmée. Les deux exclusions restent révisables si une preuve locale nouvelle est obtenue : une absence de preuve identifiée n'est pas une preuve d'absence.

## Accès et métadonnées

Le texte intégral de Flahou n'est pas confirmé : accès laissé à déterminer. L'éditeur d'Ixodes propose un accès institutionnel ou payant. Pour les six autres, une version publique de l'article a été consultée ou son accès libre confirmé chez l'éditeur. Le dépôt Zenodo/Plazi de l'article d'Amin est restreint ; son existence n'est pas la preuve d'accès retenue. `Open` décrit la consultation et ne donne pas automatiquement le droit de redistribuer le PDF.

Crossref est la source première des métadonnées DOI. La pagination d'Amin, absente de Crossref, est corroborée par PubMed et l'original : **107(2), 222–238**. Les dates de terrain ne remplacent pas les dates de publication. Les corrélations microbiome/stress et les analyses évolutives ne sont pas transformées en preuves de causalité ou de transmission locale récente.

Les deux corrections liées aux études déjà présentes sont associées dans le registre aux DOI originaux et à leurs clés Zotero. Elles ne sont pas comptées comme deux nouvelles études ; aucun champ bibliographique nécessitant une correction n'a été établi dans ce lot.

## Reprise et récupération

Résultat authentifié du 16 octobre : **427 → 435 références**, huit créations, pagination d'une notice complétée ; **relance : zéro création, huit déjà présentes, zéro nouvelle correction**. Couverture publique 8/8 dans `coverage.json`, bilan dans `execution.json`. Audit : 19 collections, 31/31 DOI du seed, zéro titre vide, doublon DOI ou doublon de titre probable détecté. Aucun échec d'import restant. Ces compteurs sont datés ; Zotero peut évoluer ensuite dans les autres conversations.

Les rapports d'exécution, instantanés, sauvegardes avant correction et fichiers d'analyse restent locaux. Le bilan final public de ce lot consigne les clés et la couverture constatée, sans secret. Pour annuler une création, inspecter d'abord la notice actuelle et ses éventuels enrichissements ; ne jamais supprimer en bloc à partir du CSV. La correction de pagination dispose d'une sauvegarde et d'un contrôle de version Zotero.

Les archives APDS et leurs pièces jointes n'ont pas été modifiées. Le hub lit Zotero au prochain rechargement ; aucun déploiement de code n'est nécessaire pour faire apparaître ces références.
