# Phase 1 figures

These figures visualize the existing 80-protein pilot (30 reference proteins and 50 test proteins). They are based on the original BLASTp and ESM-2 outputs and the recorded Colab AUC summary. No new screening experiments were run to generate these graphics.

| File | What it shows | Source |
| --- | --- | --- |
| `01_auc_comparison.png` | ROC AUC across all 50 tests, AI-designed positives vs controls, and natural positives vs controls | BLASTp and Layer 6 mean AUC verified from `results/` CSVs; Layer 6 CLS and Layer 3 max AUC from recorded Colab execution output (their complete per-protein export files are not archived here) |
| `02_blastp_sequence_matches.png` | Number of proteins with a BLASTp hit at E-value ≤ 0.01 | `results/blastp/blastp_top_matches.csv` |
| `03_roc_all_proteins.png` | ROC curves for BLASTp best bit score and ESM-2 final-layer mean pooling cosine similarity, all tests | `results/blastp/blastp_top_matches.csv`, `results/esm2/esm2_top_matches.csv` |
| `04_roc_natural_proteins.png` | The same ROC curves for 10 natural positives vs 20 negative controls | Same two CSVs |
| `05_esm2_score_overlap.png` | Per-protein cosine similarity scores for the three test groups | `results/esm2/esm2_top_matches.csv` |

**Notes**
- The BLASTp significance threshold of **E-value ≤ 0.01** describes sequence alignment significance, not a universal heme-binding classification rule.
- For ROC AUC, the scoring variables are **the maximum BLASTp bit score** and **the maximum cosine similarity to one of the 30 references**, respectively.
- The AUC summary uses fixed data subsets and matches the reported Colab outputs to three decimal places.
- The focused seven-protein follow-up was analyzed separately in Colab, and its rerun scores are not mixed into these original-output ROC figures.
- Use `python figures/generate_figures.py` at the repository root to recreate the PNG files. Requires `pandas`, `numpy`, `matplotlib`, and `scikit-learn`, plus the source CSVs in `results/`.
