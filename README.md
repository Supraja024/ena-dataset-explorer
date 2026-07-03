# ENA Dataset Explorer

A lightweight Python utility for searching the **European Nucleotide Archive (ENA)** using keyword-based queries and exploring sequencing study metadata directly from the terminal.

ENA Dataset Explorer enables researchers to quickly discover publicly available sequencing datasets and summarize important metadata such as BioProject accession, study title, sequencing methodology, sequencing platform, instrument model, organism, and sequencing run counts.

---

## Features

* Search ENA using one or more user-defined keywords.
* Retrieve matching BioProject/Study accessions.
* Display study titles and descriptions.
* Identify sequencing methodologies including:

  * Whole Genome Sequencing (WGS)
  * Whole Genome Bisulfite Sequencing (WGBS)
  * RNA Sequencing (RNA-Seq)
  * Reduced Representation Bisulfite Sequencing (RRBS)
  * ChIP-Seq
  * ATAC-Seq
  * Whole Exome Sequencing (WES)
  * Amplicon Sequencing
  * Metagenomic Sequencing
* Display:

  * BioProject accession
  * Study title
  * Organism
  * Library Strategy
  * Library Source
  * Sequencing Platform
  * Instrument Model
  * Number of sequencing runs
* Fast terminal-based output.
* No API key or authentication required.

---

## Requirements

* Python 3.8 or higher

### Install Required Package

```bash
pip install requests
```

or

```bash
pip install -r requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/ena-dataset-explorer.git
cd ena-dataset-explorer
```

Install dependencies:

```bash
pip install requests
```

---

## Usage

Open **`ena_dataset_explorer.py`** and edit the keyword list.

Example:

```python
keywords = [
    "colorectal cancer methylation",
    "breast cancer WGS",
    "Klebsiella pneumoniae colistin resistance"
]
```

Run the script:

```bash
python3 ena_dataset_explorer.py
```

---

## Example Output

```text
======================================================================
Keyword : colorectal cancer methylation
======================================================================

BioProject : PRJEB79368
Title      : Colorectal Cancer Methylome
Method     : WGBS
Source     : GENOMIC
Organism   : Homo sapiens
Platform   : ILLUMINA
Instrument : NovaSeq 6000
Runs       : 86

----------------------------------------------------------------------
```

---

## Output Information

For every matching study, the script reports:

* BioProject accession
* Study title
* Study description
* Organism
* Library strategy
* Library source
* Library selection
* Sequencing platform
* Instrument model
* Number of sequencing runs

---

## Typical Applications

* Discover publicly available sequencing datasets.
* Identify BioProjects related to a specific research topic.
* Explore genomic, transcriptomic, and epigenomic datasets.
* Compare sequencing technologies across studies.
* Build datasets for bioinformatics analyses.
* Support systematic reviews and meta-analysis studies.

---

## Project Structure

```text
ena-dataset-explorer/
│
├── ena_dataset_explorer.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## Data Source

This project retrieves metadata directly from the **European Nucleotide Archive (ENA) Portal API**.

ENA Browser:
https://www.ebi.ac.uk/ena/browser/home

ENA Portal API Documentation:
https://ena-docs.readthedocs.io/en/latest/retrieval/programmatic-access.html

---

## Limitations

* Results depend on the metadata submitted to ENA by the original data contributors.
* Some studies may contain multiple sequencing strategies, platforms, or instrument models.
* Metadata completeness varies among projects.

---

## Future Improvements

Planned enhancements include:

* Boolean keyword searching (`AND`, `OR`, `NOT`)
* CSV and Excel export
* Automatic retrieval of run accessions
* Organism-based filtering
* Library strategy filtering
* Parallel metadata retrieval for faster searches
* Interactive project selection
* Automatic dataset summary statistics

---

## License

This project is licensed under the MIT License.

---

## Citation

If you use this tool in your research, please cite the European Nucleotide Archive (ENA) as the source of sequencing metadata.

---

## Contributing

Contributions, feature requests, and bug reports are welcome. Please open an issue or submit a pull request.

---

## Author

**Supraja Mohan**

PhD Scholar
Institute of Bioinformatics (IOB), Bangalore, India

If you find this project useful, consider giving the repository a ⭐ to support future development.
