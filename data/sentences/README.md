# Monolingual Kashubian & Polish sentences

Monolingual sentences taken from Leipzig Corpora Collection ([aclanthology.org/L12-1154](https://aclanthology.org/L12-1154/)) from Wikipedia 2021.

Immediately before continued pre-training, 25% of the bytes per sentence are masked with ByT5-specific sentinel tokens ([huggingface.co/docs/transformers/model_doc/byt5](https://huggingface.co/docs/transformers/model_doc/byt5)), see `models/byt5/byt5.ipynb`.

All 10,00 Kashubian sentences are also used to generate synthetic Kashubian data (see `models/llm/openrouter-ai.ipynb`)

| Language            | Name         | trn           | dev       |
| ------------------- | ------------ | ------------- | --------- |
| Kashubian           | csb-sent     | 9,000         | 1,000     |
| Kashubian & Polish | csb-pol-sent | 4,500 & 4,500 | 500 & 500 |
