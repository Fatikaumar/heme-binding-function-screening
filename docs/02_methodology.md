# 2. Phase 1 methodology

## 2.1 Data preparation

- Assemble the 30 heme-binding references, 20 AI-designed myoglobins, 10 natural heme-binding proteins, and 20 negative controls.
- Store accession, amino-acid sequence, label and group in `data/master_dataset_80_proteins.csv`.
- Check group counts, duplicate IDs and sequences, missing sequences, length consistency, and amino-acid characters.
- Final dataset: **80 unique sequence records**.

## 2.2 BLASTp baseline

- Create a local protein BLAST database containing **only the 30 reference proteins**.
- Search the **50 test proteins** against that database using `blastp`.
- Key original search parameters:
  - Reporting E-value limit: `-evalue 10`.
  - Retain one high-scoring segment per query/reference pair: `-max_hsps 1`.
  - Tabular fields: query ID, subject ID, percent identity, alignment length, query length, query start/end, E-value, and bit score.
- For each test protein, retain the highest-bit-score reference match.
- Calculate query coverage from the reported aligned query span divided by total query length.
- Use **E-value ≤ 0.01** to describe a statistically significant sequence match in the fixed reference search.
- Use each protein's **best BLASTp bit score**, not the E-value yes/no flag, for ROC AUC analysis.

**Reference length consistency check:** ESM-2 used the first 1,022 residues of human NOS3 (`P29474`), which is 1,203 residues in the dataset. BLASTp was rerun with this same shortened reference. Its three reported subgroup AUC values were unchanged to three decimals.

## 2.3 ESM-2 embeddings

- Model: pretrained `facebook/esm2_t6_8M_UR50D` (six transformer layers, approximately 8 million parameters; 320-dimensional hidden state).
- Input: the same 80 amino-acid sequences; truncate to the first **1,022 amino acids** when longer.
- Extract residue representations directly from transformer hidden states, excluding beginning/end special tokens for residue pooling.
- Compare the following whole-protein representations:
  - Layer 6, **mean pooling** across residues.
  - Layer 6, **first special-token (CLS/BOS) representation**.
  - Layer 3, **mean pooling** across residues.
  - Layer 3, **max pooling** across residues, dimension by dimension.
- For each test protein, calculate cosine similarity against all 30 reference vectors; retain the **maximum similarity** as its score.
- The pretrained model was used without task-specific fine-tuning.

## 2.4 Evaluation

- The primary discrimination metric is **ROC AUC**, based on each method's continuous per-protein score.
- Report AUC on (a) all 30 positives vs 20 controls; (b) 20 designed positives vs 20 controls; and (c) 10 natural positives vs 20 controls.
- Evaluate the seven natural proteins with BLASTp E-values **greater than 0.01** separately, against the same 20 controls.
- In that focused analysis, report how many positives score above a cutoff set from the negative-control scores to flag **one of 20 controls** (an observed 5% false-alarm rate).
- As an additional check, compare protein length against Layer 3 max-pooling similarity using Spearman rank correlation and a length-only AUC.

## 2.5 Data and software provenance

- Dataset: `data/master_dataset_80_proteins.csv`.
- Original BLASTp exports: `results/blastp/`.
- Original ESM-2 mean-pooling exports: `results/esm2/`.
- Consolidated analysis notebooks: `notebooks/`.
- Later layer/pooling and matched-reference experiments were run in Colab; their reported numerical outputs are documented here. Not all later per-protein CSV exports have been added to `results/`.

A BLASTp alignment score measures sequence similarity; an ESM-2 cosine score measures embedding similarity. Neither directly measures biochemical heme binding.
