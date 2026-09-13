
Our ByT5 checkpoints (on HuggingFace): https://huggingface.co/collections/livles/slavic-byt5-for-kashubian-inflection

Base Model: ByT5 small (https://aclanthology.org/2022.tacl-1.17/)

# Low-Resource Morphological Inflection For Kashubian



Kashubian, a low-resource Slavic language, lacks sufficient annotated pairs for generating inflected word forms. To address this data scarcity, we fine-tune the byte-level transformer ByT5 on datasets from 7 related languages. We also continue pre-training on Kashubian and Polish monolingual corpora, and generate synthetic Kashubian word forms using LLM annotations. Multilingual fine-tuning and continued pre-training improve the monolingual ByT5 accuracy by 4–5 points, while incorporating synthetic data exceeds the previous strongest baseline by 10 points. Training ByT5 on multilingual task datasets, monolingual sentences with self-supervision, and LLM-annotated data yields strong relative accuracy gains for the low-resource morphological inflection of Kashubian.

## Models
* ByT5 (https://aclanthology.org/2022.tacl-1.17/): fine-tuning, continued pre-training
* LLMs Gemini 2.5 Flash (https://arxiv.org/abs/2507.06261) and GPT-OSS 120B (https://arxiv.org/abs/2508.10925): zero-shot, data generation
* SIGMORPHON-UniMorph 2023 shared task baselines (https://aclanthology.org/2023.sigmorphon-1.13/): fine-tuning

## Data
### Fine-tuning
* SIGMORPHON 2023 shared task (https://aclanthology.org/2023.sigmorphon-1.13/): morphological inflection data in UniMorph 4.0 schema
* Legacy UniMorph (https://unimorph.github.io/): morphological inflection data from all UniMorph releases
### Continued pretraining / synthetic data generation
* Leipzig Corpora Collection (https://aclanthology.org/L12-1154/): sentences from Wikipedia 2021 in Kashubian and Polish
