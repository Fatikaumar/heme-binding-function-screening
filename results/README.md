# Results — Phase 1 heme-binding screening pilot

This folder preserves the initial result files from comparisons of 50 test proteins against 30 heme-binding references, using BLASTp and ESM-2 (facebook/esm2_t6_8M_UR50D).

## Files

- `blastp/blastp_all_hits.csv`: All BLASTp alignments reported for the 50 test proteins against 30 references (original search; E-value reporting limit 10).
- `blastp/blastp_top_matches.csv`: Highest-bit-score BLASTp alignment per test protein, with identity, coverage, E-value, and bit score.
- `esm2/esm2_all_similarities.csv`: Full 50 x 30 cosine similarity table from final-layer, mean-pooled ESM-2 embeddings.
- `esm2/esm2_top_matches.csv`: Highest cosine-similarity reference per test protein from that original ESM-2 run.
- `comparison/blastp_esm2_comparison.xlsx`: Initial side-by-side comparison workbook of BLASTp and final-layer mean-pooled ESM-2.

## Subsequent experiments

The project also ran a BLASTp sensitivity check using NOS3 shortened to 1,022 amino acids, and ESM-2 CLS, Layer 3 mean, and Layer 3 max pooling comparisons. Those **later per-protein CSV exports are not included in this package** because they were not present among the available source files; do not mistake the initial results above for those later experiments.

The AUC results reported in the Colab outputs were:

| Scoring method | All positives vs negatives | AI-designed vs negatives | Natural vs negatives |
|---|---:|---:|---:|
| BLASTp best bit score | 0.905 | 1.000 | 0.715 |
| ESM-2 Layer 6 mean pooling | 0.517 | 0.512 | 0.525 |
| ESM-2 Layer 6 CLS pooling | 0.542 | 0.522 | 0.580 |
| ESM-2 Layer 3 mean pooling | 0.542 | 0.547 | 0.530 |
| ESM-2 Layer 3 max pooling | 0.753 | 0.802 | 0.655 |

Focused analysis: for the seven natural heme-binding proteins without BLASTp E <= 0.01, AUCs against the 20 negative controls were BLASTp 0.593, ESM-2 Layer 3 mean 0.486, and ESM-2 Layer 3 max 0.586. At the in-sample cutoff permitting one negative above threshold, detection counts were respectively 0/7, 1/7, and 1/7.

These summary metrics are transcribed from the Colab outputs shared during the study; the underlying raw ESM-2 Layer 3 max-pooling CSV and matched-length BLASTp CSV should be added when available. The detailed analysis can be regenerated using `notebooks/02_blastp_analysis.ipynb`, `notebooks/03_esm2_analysis.ipynb`, and `notebooks/04_performance_evaluation.ipynb`.
