# 1. Research overview

**Title:** Evaluating Protein Language Models for Function-Based Screening of Heme-Binding Proteins Against Traditional Sequence-Search Methods

## Research question

Can protein language model representations identify heme-binding proteins with divergent amino-acid sequences that traditional sequence-search methods may miss, without increasing false-positive predictions?

## Biological target

Heme binding is the target property. This is **not** a study of myoglobin alone, nor of oxygen transport in general. The reference collection contains several heme-binding protein families with different biological roles.

## Dataset

| Group | Number | Role |
|---|---:|---|
| Heme-binding references | 30 | Fixed reference collection for both search methods |
| AI-designed myoglobins | 20 | Positive test examples (`dnMb02`–`dnMb21`) |
| Natural heme-binding proteins | 10 | Positive test examples from different families |
| Negative controls | 20 | Comparison group for selectivity |
| **Total** | **80** | **30 references + 50 tests** |

The 20 designed sequences were derived from the supplementary material accompanying Sumida et al. (2024), *Improving Protein Expression, Stability, and Function with ProteinMPNN*. The 60 other sequences were retrieved using accession identifiers; accession, source and sequence columns are included in the master dataset.

Study source: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10811672/>

## Phase 1 objectives

- Establish BLASTp sequence-search performance using a fixed 30-protein reference collection.
- Assess whether pretrained ESM-2 whole-protein representations can rank heme-binding test proteins above the controls.
- Examine separately the AI-designed myoglobins and natural heme-binding proteins.
- Investigate the natural proteins with no significant BLASTp match to the fixed reference set.

## Repository map

- `data/`: protein sequences, identifiers and group labels.
- `notebooks/`: Colab workflows for dataset preparation, BLASTp, ESM-2 and evaluation.
- `results/`: available original output files and summary tables.
- `figures/`: plots and their generation script.
- `docs/`: the study narrative and methodological record.
