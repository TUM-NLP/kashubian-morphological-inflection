# Data

This directory contains Slavic morphological inflection datasets in the UniMorph 4.0 schema (as defined in https://aclanthology.org/2022.lrec-1.89/) as well as Kashubian (and Polish) monolingual sentences used for pre-training and synthetic Kashubian data generation. Data is taken from the SIGMORPHON–UniMorph 2023 Shared Task (https://aclanthology.org/2023.sigmorphon-1.13/), legacy UniMorph datasets (https://unimorph.github.io/) reformatted for schema consistency, and the Leipzig Corpora Collection ([aclanthology.org/L12-1154](https://aclanthology.org/L12-1154/)).

- `./baselines-data`: 2023 shared task data + updated data from previous UniMorph releases (UniMorph 4.0) + synthetic Kashubian data, in triplet format
- `./data-preprocessing`: Data-preprocessing (down-sampling UniMorph data, transforming feature schema to UniMorph 4.0, turning to .tsv or .json Lines format for ByT5)
- `./byt5-data`: Fine-tuning data for chosen Slavic languages and monolingual sentences from Kashubian and Polish corpora for ByT5
