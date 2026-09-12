# Low-Resource Morphological Inflection For Kashubian

* ByT5 Model Checkpoints (HuggingFace): https://huggingface.co/collections/livles/slavic-byt5-for-kashubian-inflection
* Base Model: ByT5 small (https://huggingface.co/google/byt5-small)

## Models

* SIGMORPHON-UniMorph 2023 shared task baselines: `./models/inflectionSTbaselines`
* ByT5:  `./models/ByT5`
* LLMs Gemini 2.5 Flash and GPT-OSS 120B: `./models/llm` (zero-shot, data generation)

### Data

* Task data: `./data/sigmorphon-data` (triplet: (lemma, features, target))
* Data preprocessing: `./data/data-preprocessing` (combining data, transforming feature schema, converting to ByT5 prompt)

### ByT5

ByT5 Model Checkpoints (HuggingFace): https://huggingface.co/collections/livles/slavic-byt5-for-kashubian-inflection

Base Model: ByT5 small (https://huggingface.co/google/byt5-small)

### ByT5: Fine-Tuned

| Model                                  | Base Model                                              | Training Data                     | train | dev | test |
| -------------------------------------- | ------------------------------------------------------- | --------------------------------- | ----- | --- | ---- |
| pol                                    | ByT5                                                    | pol                               |       |     |      |
| ces                                    | ByT5                                                    | ces                               |       |     |      |
| slk                                    | ByT5                                                    | slk                               |       |     |      |
| dsb                                    | ByT5                                                    | dsb                               |       |     |      |
| slavic                                 | ByT5                                                    | pol, ces, slk, dsb                |       |     |      |
| slavic-word                            | ByT5                                                    | pol, ces, slk, dsb                |       |     |      |
| slavic-word-or-family                  | ByT5                                                    | pol,ces,slk,dsb                   |       |     |      |
| slavic-dist                            | ByT5                                                    | pol, ces, slk, dsb, bel, rus, mkd |       |     |      |
| slavic-dist-word                       | ByT5                                                    | pol, ces, slk, dsb, bel, rus, mkd |       |     |      |
| slavic-dist-word-or-family             | ByT5                                                    | pol, ces, slk, dsb, bel, rus, mkd |       |     |      |
| csb-sent-25perc-byte-**pol**     | csb-sent-25perc-byte (ByT5 continued pretrained)       | pol                               |       |     |      |
| csb-pol-sent-25perc-byte-**pol** | csb-pol-sent-25perc-byte (ByT5 continued pretrained ) | pol                               |       |     |      |

### ByT5: Continued Pretrained

| Model                    | Base Model | Corpus              | train: sentences | dev: sentences |
| ------------------------ | ---------- | ------------------- | ---------------- | -------------- |
| csb-pol-sent-25perc-byte | ByT5       | Kashubian           | 9,000            | 1,000          |
| csb-sent-25perc-byte     | ByT5       | Kashubian & Polish | 4,500 & 4,500    | 500 & 500      |
