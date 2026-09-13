# Data
This repository contains Slavic morphological inflection datasets in the UniMorph 4.0 schema (https://aclanthology.org/2022.lrec-1.89/). It includes data from the SIGMORPHON–UniMorph 2023 Shared Task (https://aclanthology.org/2023.sigmorphon-1.13/) as well as legacy UniMorph datasets (https://unimorph.github.io/) reformatted for schema consistency.

- `./sigmorphon/data`: 2023 Shared task data + updated data from previous UniMorph releases (UniMorph 4.0) + synthetic Kashubian data, in triplet format
- `./data-preprocessing`: Data-preprocessing (down-sampling UniMorph data, transforming feature schema to UniMorph 4.0, turning to .tsv or .json Lines format for ByT5)
