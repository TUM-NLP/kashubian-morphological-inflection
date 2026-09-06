# Models
- `./ByT5`: Experiments with ByT5
- `./llm`: Zero-Shot prompting with GPT-OSS-120B and Gemini 2.5 Flash

# Data 
- `./2023InflectionST`: 2023 Shared task data + updated data from previous UniMorph releases, in triplet format
- `./data/processing/preprocessing`: Data data/processing/preprocessing 
- `./postprocessing`: Data post-processing (used for evaluation on mixed datasets)
- `./error_analysis_lucy`: contains source code and output used for error analysis

# Low-Resource Morphological Inflection For Kashubian
ByT5 Model Checkpoints (HuggingFace): https://huggingface.co/collections/livles/slavic-byt5-for-kashubian-inflection

Base Model: ByT5 small (https://huggingface.co/google/byt5-small)
## Model Overview
|Model|Trained Model|Training Data|
|-|-|-|
|pol|ByT5|pol|
|ces|ByT5|ces|
|slk|ByT5|slk|
|dsb|ByT5|dsb|
|slavic|ByT5|pol,ces,slk,dsb|
|slavic-word|ByT5|pol,ces,slk,dsb|
|slavic-word-or-family|ByT5|pol,ces,slk,dsb|
|slavic-dist|ByT5|pol,ces,slk,dsb,bel,rus,mkd|
|slavic-dist-word|ByT5|pol,ces,slk,dsb,bel,rus,mkd|
|slavic-dist-word-or-family|ByT5|pol,ces,slk,dsb,bel,rus,mkd|
|csb-sent-25perc-byte-pol|ByT5|pol,ces,slk,dsb,bel,rus,mkd|
|csb-pol-sent-25perc-byte-pol|ByT5|pol, csb sentences|
|csb-pol-byte-25perc-sent-pol|ByT5|pol, csb + pol sentences|

