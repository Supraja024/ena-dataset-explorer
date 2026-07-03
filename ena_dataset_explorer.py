#!/usr/bin/env python3

"""
ENA Keyword Finder
Search ENA projects by keyword and display study details.

Requirements:
    pip install requests

Author: ChatGPT
"""

import requests
from collections import Counter

# ============================================================
# EDIT YOUR SEARCH KEYWORDS HERE
# ============================================================

keywords = [
    "colorectal cancer methylation",
    "breast cancer WGS",
    "Klebsiella pneumoniae colistin resistance"
]

# ============================================================

BASE_URL = "https://www.ebi.ac.uk/ena/portal/api/search"


def ena_search(result, query, fields):
    params = {
        "result": result,
        "query": query,
        "fields": fields,
        "format": "json"
    }

    r = requests.get(BASE_URL, params=params, timeout=60)
    r.raise_for_status()
    return r.json()


for keyword in keywords:

    print("\n" + "=" * 70)
    print(f"Keyword : {keyword}")
    print("=" * 70)

    # Search studies
    query = f'study_title="{keyword}" OR description="{keyword}"'

    try:
        studies = ena_search(
            "study",
            query,
            "study_accession,study_title,description,scientific_name"
        )
    except Exception as e:
        print(e)
        continue

    if len(studies) == 0:
        print("No studies found.\n")
        continue

    for study in studies:

        project = study["study_accession"]

        try:
            experiments = ena_search(
                "read_experiment",
                f'study_accession="{project}"',
                ",".join([
                    "library_strategy",
                    "library_source",
                    "library_selection",
                    "instrument_platform",
                    "instrument_model",
                    "run_accession"
                ])
            )

        except Exception:
            experiments = []

        strategies = Counter()
        sources = Counter()
        platforms = Counter()
        instruments = Counter()

        runs = set()

        for exp in experiments:
            if exp.get("library_strategy"):
                strategies[exp["library_strategy"]] += 1

            if exp.get("library_source"):
                sources[exp["library_source"]] += 1

            if exp.get("instrument_platform"):
                platforms[exp["instrument_platform"]] += 1

            if exp.get("instrument_model"):
                instruments[exp["instrument_model"]] += 1

            if exp.get("run_accession"):
                runs.add(exp["run_accession"])

        method = ", ".join(strategies.keys()) if strategies else "Unknown"
        source = ", ".join(sources.keys()) if sources else "Unknown"
        platform = ", ".join(platforms.keys()) if platforms else "Unknown"
        instrument = ", ".join(instruments.keys()) if instruments else "Unknown"

        print(f"""
BioProject : {project}
Title      : {study.get('study_title','NA')}
Method     : {method}
Source     : {source}
Organism   : {study.get('scientific_name','NA')}
Platform   : {platform}
Instrument : {instrument}
Runs       : {len(runs)}
""")

        print("-" * 70)

print("\nSearch completed.\n")
