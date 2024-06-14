# DNA Analyzer

## Introduction

Your job is to write Python code to generate a report on the statistical occurrences of various amino acids in a given string.

## Prerequisites

Completion of this task requires the use of pure `Python 3` with no additional frameworks or libraries. 

## Task Details

Note: Please do *NOT* modify any tests unless specifically told to do so.

Please implement the `get_amino_acids_report` method in the `app.dna_analyser.DNAAnalyser` class.

This method should split the `dna_sequence` argument into 3-characters long substrings.
Each substring is a codon specifying an amino acid. Based on the data from the `codon.tsv` file count amino acids occurrences in the given sequence.
Please keep in mind that the `dna_sequence` argument might not be valid, e.g. its length could not be a multiple of the number 3.

The method should return a dictionary with amino acids name as keys and their count as values.
If the sequence is not of length 3, omit it.

#### Example

For input sequence `AAATTTGGGAAA` and `codon.tsv` file with following content:

```
AAA    Lysine
GGG    Glycine
TTT    Phenylalanine
```

This method should return a dictionary like the one below.

```json
{
  'Lysine': 2,
  'Phenylalanine': 1,
  'Glycine': 1
}
```

## Hints

You shouldn't modify the unit tests.

To execute the unit tests, use:

```
pip install -q -e . && python3 setup.py pytest
```
