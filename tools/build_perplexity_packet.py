"""Build a portable, source-unverified packet for the Perplexity SUP review."""
import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "reviews" / "communication-supplement-2026-10-25"
EXCLUDED = {"SUP-04", "SUP-27", "SUP-51", "SUP-57", "SUP-64", "SUP-65"}


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=REVIEW / "PERPLEXITY-VERIFICATION-PACKET-64.md",
    )
    args = parser.parse_args()
    sources = rows(REVIEW / "reported-sources.tsv")
    selected = [row for row in sources if row["id"] not in EXCLUDED]
    if len(sources) != 70 or len(selected) != 64 or len({row["id"] for row in selected}) != 64:
        raise ValueError("Expected 70 SUP entries and exactly 64 entries to review")
    relations = [row for row in rows(REVIEW / "local-relations.tsv") if row["id"] not in EXCLUDED]
    lines = [
        "# Paquet de vérification Perplexity — 64 entrées SUP",
        "",
        "Ce paquet fournit les 64 entrées à vérifier du supplément Communication Dzanga-Sangha.",
        "Il a été extrait localement du registre de conservation le 2 novembre 2026.",
        "Tous les éléments ci-dessous sont des déclarations rapportées, non des métadonnées déjà vérifiées.",
        "Les URL servent de pistes : une URL rapportée ne prouve ni son accessibilité actuelle, ni les champs bibliographiques associés.",
        "",
        "## Consignes de sécurité documentaire",
        "",
        "- Vérifier uniquement les 64 blocs ci-dessous, avec des sources réellement consultées.",
        "- Ne pas inventer date, auteur, langue, durée, pagination, droits ou relation entre versions.",
        "- Un rapprochement indiqué plus bas est seulement un candidat ; aucune fusion ni déduplication automatique.",
        "- Ne pas proposer d'import Zotero, de modification Git ou de publication.",
        "- Si une source est inaccessible, conserver `blocked` ou `partial` plutôt que compléter par inférence.",
        "",
        "## Format de retour requis",
        "",
        "Produire un TSV, une ligne par identifiant, avec les colonnes exactes suivantes :",
        "",
        "```text",
        "id\tstatus\ttitle_confirmed\tcreator_confirmed\tdate_confirmed\ttype_confirmed\tsource_url\tevidence_summary\tdzanga_relevance\trelationship_or_duplicate\tlimitations\tchecked_at",
        "```",
        "",
        "Les seuls statuts admis sont `verified_delegated`, `partial`, `blocked` et `duplicate_candidate`.",
        "Un résultat incomplet doit rester une ligne avec ses limites explicites. Si l'interface ne permet pas de produire des fichiers, renvoyer le TSV complet dans un bloc de code, puis un README Markdown séparé ; ne pas prétendre qu'un téléchargement a été créé.",
        "",
        "## Six entrées déjà traitées — à exclure",
        "",
        "- SUP-04 : partiel ; date d'en-tête non validée.",
        "- SUP-27 : bloqué ; page et sommaire WWF non récupérés.",
        "- SUP-51 : métadonnées déléguées confirmées (Los Angeles Times, 1994).",
        "- SUP-57 : partiel ; versions EN/FR consultées, année éditoriale non confirmée.",
        "- SUP-64 : partiel ; référence secondaire Chadwick, original National Geographic non retrouvé.",
        "- SUP-65 : partiel ; CARPO/WWF confirmé en partie, fin de l'entretien et identité complète non établies.",
        "",
        "## Rapprochements locaux seulement (ne sont pas des identités démontrées)",
        "",
        "| SUP | Candidat local | Relation rapportée | Limite |",
        "| --- | --- | --- | --- |",
    ]
    if relations:
        for relation in relations:
            note = relation["review_note"].replace("|", "\\|")
            lines.append(f"| {relation['id']} | {relation['target_id']} | {relation['relation']} | {note} |")
    else:
        lines.append("| Aucun | — | — | — |")
    lines.extend(["", "## Blocs sources exacts à examiner", ""])
    for row in selected:
        raw = json.loads(row["raw_block_json"])
        lines.extend([raw, ""])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(json.dumps({"output": str(args.output), "entries": len(selected), "relations": len(relations)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
