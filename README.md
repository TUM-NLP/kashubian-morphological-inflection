# Low-Resource Morphological Inflection For Kashubian

* ByT5 Model Checkpoints (HuggingFace): https://huggingface.co/collections/livles/slavic-byt5-for-kashubian-inflection
* Base Model: ByT5 small (https://aclanthology.org/2022.tacl-1.17/)
* SIGMORPHON-UniMorph 2023 shared task 0 part 1: https://aclanthology.org/2023.sigmorphon-1.13/

## Models

* SIGMORPHON-UniMorph 2023 shared task baselines : `./models/inflectionSTbaselines`
* ByT5:  `./models/ByT5`
* LLMs Gemini 2.5 Flash and GPT-OSS 120B: `./models/llm` (zero-shot, data generation)

### Data

* Task data: `./data/sigmorphon-data` (triplet: (lemma, features, target))
* Data preprocessing: `./data/data-preprocessing` (combining data, transforming feature schema, converting to ByT5 prompt)
