# 3. Phase 1 results

## 3.1 Significant BLASTp reference matches

The significance threshold was **E-value ≤ 0.01** in the search against the fixed 30-reference database.

| Test group | Significant matches / total |
|---|---:|
| AI-designed myoglobins | 20 / 20 |
| Natural heme-binding proteins | 3 / 10 |
| Negative controls | 2 / 20 |

The two negative controls with significant *sequence matches* were:

| Protein | Best-hit E-value | Bit score | Identity | Query coverage |
|---|---:|---:|---:|---:|
| C-phycocyanin alpha | 0.004 | 26.9 | 27.4% | 52.5% |
| Green fluorescent protein | 0.005 | 28.1 | 22.6% | 45.0% |

These are alignment hits, **not** experimentally established heme-binding predictions.

## 3.2 Head-to-head ROC AUC

Each score is the highest similarity to any of the 30 references: the best **bit score** for BLASTp or the highest **cosine similarity** for ESM-2.

| Method | All positives vs controls | Designed positives vs controls | Natural positives vs controls |
|---|---:|---:|---:|
| BLASTp best bit score | **0.905** | **1.000** | **0.715** |
| ESM-2 Layer 6 mean pooling | 0.517 | 0.512 | 0.525 |
| ESM-2 Layer 6 CLS/BOS | 0.542 | 0.522 | 0.580 |
| ESM-2 Layer 3 mean pooling | 0.542 | 0.547 | 0.530 |
| ESM-2 Layer 3 max pooling | 0.753 | 0.802 | 0.655 |

**Main observation:** Layer 3 max pooling was substantially better than mean pooling on this dataset, but BLASTp ranked positives above controls more successfully in all three group comparisons.

## 3.3 Focused set: natural positives without significant BLASTp matches

Seven natural heme-binding proteins had no significant match to the fixed 30-reference BLASTp database at the selected threshold:

`DppA`, `CyoB`, `HutZ`, `IsdA`, `NirN`, `Rv0203`, `CtaA`.

The corresponding analysis included **7 positive test proteins and the same 20 negative controls**.

| Scoring method | ROC AUC | Positives detected | Controls flagged |
|---|---:|---:|---:|
| BLASTp best bit score | 0.593 | 0 / 7 | 1 / 20 |
| ESM-2 Layer 3 mean pooling | 0.486 | 1 / 7 | 1 / 20 |
| ESM-2 Layer 3 max pooling | 0.586 | 1 / 7 | 1 / 20 |

At the reported empirical operating point, mean pooling selected **HutZ**, whereas max pooling selected **CtaA**.

**Main observation:** This experiment did **not** demonstrate a clear advantage for whole-protein ESM-2 embedding similarity over BLASTp on the seven selected cases.

## 3.4 Protein-length check

- Spearman correlation between protein length and Layer 3 max similarity: **−0.239** across all 50 test proteins.
- Within the designed positives: **−0.064**; natural positives: **−0.248**; negative controls: **−0.308**.
- Length-only AUCs (with greater length indicating a positive): **0.344** overall, **0.175** for designed positives vs controls, **0.682** for natural positives vs controls.

There was no positive length–similarity correlation in these data; length differences between protein groups nevertheless remain relevant.

## 3.5 Sequence-length consistency check

BLASTp was rerun with reference `P29474` shortened from 1,203 to 1,022 residues, matching the ESM-2 input. BLASTp AUC results remained **0.905**, **1.000**, and **0.715** for the overall, designed and natural comparisons, respectively (to three decimal places).

## Summary

In this Phase 1 study, the tested whole-protein ESM-2 representations did not outperform the BLASTp sequence-search baseline. The result applies to the specific reference collection, labels, proteins and scoring rules evaluated here.
