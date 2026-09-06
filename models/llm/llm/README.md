# Source code
- `openrouter-ai.ipynb` (output is stored in `./data`)

All LLMs are accessed via [openrouter.ai](https://openrouter.ai/).
# 1. Zero-Shot Morphological Inflection using large-scale LLMs
## Models: Large Scale LLMs:
- Gemini 2.5 Flash 
- GPT-OSS 120B
## Inference 
- Output: `/data/<model_name>/csb_<model_name>.out`

# 2. Synthetic Kashubian fine-tuning: Generating synthetic Kashubian task data using Gemini from Kashubian corpus
- synthetic Kashubian task data: `data/csb.{trn,dev}`

Gemini extracts inflected words (**target**) from **Kashubian sentences** and predicts the root form (**lemma**) and the morphosyntactic **features** of the inflected word. These are the (lemma, features, target) triplets for the **synthetic Kashubian** data.

The synthetic samples are reduced by invalid forms (see acceptance critia below) and down-sampled to 10,000 samples.
The synthetic Kashubian data is then used to fine-tune ByT5 (variant: fine-tuning additionally with Polish SIGMORPHON inflection data).

## Source Models: 
- LLM: Gemini 2.5 Flash
- Base fine-tuning model: ByT5 small
## Fine-Tuned Model
ByT5: hier-csb-gemini 
(variant: hier-csb-pol)
## Source data: Monolingual Kashubian corpus
Leipzig Corpora Collection (https://aclanthology.org/L12-1154/): 10k Kashubian sentences (Wikipedia 2021)
## Synthetic Data: Acceptance criteria
1. Removing Gemini's answers with longer text outputs such as sentences
2. Deleting lines with wrong feature formats: N	Case=Nom|Gender=Fem|Number=Sing	Bòliwiô
## Synthetic Data: Down-sampling
- Output: `/data/csb.{trn,dev}`

After filtering the synthetic data for following acceptance criteria, *10,000 samples* are randomly sampled for the final *synthetic Kashubian* dataset.


