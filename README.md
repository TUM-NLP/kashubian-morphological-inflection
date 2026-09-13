# Low-Resource Morphological Inflection For Kashubian

* SIGMORPHON-UniMorph 2023 shared task 0 part 1: https://aclanthology.org/2023.sigmorphon-1.13/
* ByT5 Model Checkpoints (HuggingFace): https://huggingface.co/collections/livles/slavic-byt5-for-kashubian-inflection
* Base Model: ByT5 small (https://aclanthology.org/2022.tacl-1.17/)

## Models
* SIGMORPHON-UniMorph 2023 shared task baselines (https://aclanthology.org/2023.sigmorphon-1.13/): fine-tuning
* ByT5 (https://aclanthology.org/2022.tacl-1.17/): fine-tuning, continued pre-training
* LLMs Gemini 2.5 Flash (https://arxiv.org/abs/2507.06261) and GPT-OSS 120B (https://arxiv.org/abs/2508.10925): zero-shot, data generation

## Data
### Fine-tuning
* SIGMORPHON 2023 shared task (https://aclanthology.org/2023.sigmorphon-1.13/): morphological inflection data in UniMorph 4.0 schema
* Legacy UniMorph (https://unimorph.github.io/): morphological inflection data from all UniMorph releases
### Continued pretraining / synthetic data generation
* Leipzig Corpora Collection (https://aclanthology.org/L12-1154/): sentences from Wikipedia 2021 in Kashubian and Polish
