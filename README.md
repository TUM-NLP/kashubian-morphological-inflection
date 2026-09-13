# Low-Resource Morphological Inflection For Kashubian

* ByT5 Model Checkpoints (HuggingFace): https://huggingface.co/collections/livles/slavic-byt5-for-kashubian-inflection
* Base Model: ByT5 small (https://aclanthology.org/2022.tacl-1.17/)

## Models

* SIGMORPHON-UniMorph 2023 shared task baselines (https://aclanthology.org/2023.sigmorphon-1.13/): `./models/inflectionSTbaselines`
* ByT5 (https://aclanthology.org/2022.tacl-1.17/):  `./models/ByT5`
* LLMs Gemini 2.5 Flash (https://arxiv.org/abs/2508.10925) and GPT-OSS 120B (https://arxiv.org/abs/2507.06261): `./models/llm` (zero-shot, data generation)

### Data

* Task data: `./data/sigmorphon-data` (triplet: (lemma, features, target))
* Data preprocessing: `./data/data-preprocessing` (combining data, transforming feature schema, converting to ByT5 prompt)
