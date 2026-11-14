# 4. Limitations and proposed next phase

## Limitations

- **Negative labels:** The 20 negative controls were selected from proteins without established heme-binding functions; they were **not independently experimentally confirmed to be non-binders**. Thus, apparent false alarms are provisional.
- **Related designs:** All 20 AI-designed positives derive from a myoglobin design scaffold. Their detection does not establish performance on designs intended to evade sequence screening.
- **Small natural subset:** Only 10 natural positives were included; the focused subset has 7. Estimates therefore have limited precision.
- **BLAST-selected focused subset:** The seven natural proteins were chosen because their BLASTp E-values exceeded 0.01. This is a targeted failure-case analysis, not an independent unbiased method comparison.
- **Threshold estimation:** The observed one-in-20 control-flagging cutoff was selected using the same controls assessed in the results; it is not an independently validated operating point.
- **Reference scope:** BLASTp searches used a fixed reference collection of 30 proteins, not the full UniProt database; database size influences E-values.
- **Biochemical scope:** Heme interaction includes different roles, locations, cofactors and binding mechanisms. Treating all examples as one binary task can obscure mechanistic diversity.
- **Embedding scope:** The ESM-2 analysis used a small, pretrained model and simple global pooling. It did not train a heme-binding classifier or isolate a validated function-specific feature.
- **Input truncation:** The first 1,022 amino acids of long proteins were used for ESM-2. The matched-length BLASTp rerun preserved AUC to three decimals, but that does not establish every individual alignment was unchanged.

## Phase 1 conclusion

Whole-protein ESM-2 cosine similarity did not show a clear ranking or detection advantage over BLASTp on the examined natural proteins without significant BLASTp matches. Different pooling strategies affected performance, but did not overturn this conclusion.

## Proposed Phase 2: Local, residue-level representations

**Hypothesis:** Information related to heme binding may be more detectable in ESM-2 residue-level representations associated with experimentally characterised heme-binding regions than in globally pooled protein vectors.

**Proposed workflow (not yet performed):**

1. Identify experimentally characterised heme-binding residues/regions in suitable **reference proteins only**.
2. Specify a reproducible method to extract or compare residue-level ESM-2 representations without relying on test-protein binding-site labels.
3. Compare against the **same BLASTp and whole-protein ESM-2 baselines**.
4. Report performance on the same natural positives and negative controls, including failure cases.

Phase 2 is a proposed extension, **not** an existing experimental finding.
