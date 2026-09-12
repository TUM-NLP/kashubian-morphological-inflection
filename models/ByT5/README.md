# ByT5

- Model Checkpoints (HuggingFace): https://huggingface.co/collections/livles/slavic-byt5-for-kashubian-inflection

* Base Model: ByT5 small (https://huggingface.co/google/byt5-small)

- Code: `byt5.ipynb`contains code for pre-training, fine-tuning and testing the ByT5-small (inference outputs in `output_byt5_small/`)
- Data in ByT5's format: `../../data/data-preprocessing/preprocessing_to_json_or_tsv/data`

### ByT5: Fine-Tuned

* Original task data: `../../data/sigmorphon-data`

| Model                                  | Base Model                                              | Training Data                     | train  | dev   |
| -------------------------------------- | ------------------------------------------------------- | --------------------------------- | ------ | ----- |
| **pol**                               | ByT5                                                    | pol                               | 10,000 | 1,000 |
| **ces**                               | ByT5                                                    | ces                               | 10,000 | 1,000 |
| **slk**                               | ByT5                                                    | slk                               | 10,000 | 1,000 |
| **dsb**                               | ByT5                                                    | dsb                               | 10,000 | 1,000 |
| **slavic**                            | ByT5                                                    | pol, ces, slk, dsb                | 40,000 | 4,000 |
| **slavic**-word                       | ByT5                                                    | pol, ces, slk, dsb                | 40,000 | 4,000 |
| **slavic**-word-or-family             | ByT5                                                    | pol,ces,slk,dsb                   | 40,000 | 4,000 |
| **slavic-dist**                       | ByT5                                                    | pol, ces, slk, dsb, bel, rus, mkd | 70,000 | 7,000 |
| **slavic-dist**-word                  | ByT5                                                    | pol, ces, slk, dsb, bel, rus, mkd | 70,000 | 7,000 |
| **slavic-dist**-word-or-family        | ByT5                                                    | pol, ces, slk, dsb, bel, rus, mkd | 70,000 | 7,000 |
| csb-sent-25perc-byte-**pol**     | csb-sent-25perc-byte (ByT5 continued pretrained)       | pol                               | 10,000 | 1,000 |
| csb-pol-sent-25perc-byte-**pol** | csb-pol-sent-25perc-byte (ByT5 continued pretrained ) | pol                               | 10,000 | 1,000 |

### ByT5: Continued Pretrained

* Corpora:  Leipzig Corpora Collection (Wikipedia 2021) [aclanthology.org/L12-1154](https://aclanthology.org/L12-1154/)

| Model                    | Base Model | Corpus              | train: sentences | dev: sentences |
| ------------------------ | ---------- | ------------------- | ---------------- | -------------- |
| csb-pol-sent-25perc-byte | ByT5       | Kashubian           | 9,000            | 1,000          |
| csb-sent-25perc-byte     | ByT5       | Kashubian & Polish | 4,500 & 4,500    | 500 & 500      |
