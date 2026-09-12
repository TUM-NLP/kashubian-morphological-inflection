Task data in (lemma, features, target) format, UniMorph 4.0, similar to SIGMORPHON UniMorph Shared Task 0 data

# Monolingual

| Language name                                    | Language code           | Data modification                           | trn                     | dev                    | test  |
| ------------------------------------------------ | ----------------------- | ------------------------------------------- | ----------------------- | ---------------------- | ----- |
| Kashubian                                        | csb                     | Features converted to UniMorph 4.0          | (synthetic)<br />10,000 | (synthetic)<br />1,000 | 509   |
| Polish, Czech, Slovak, Lower Sorbian, Macedonian | pol, ces, slk, dsb, mkd | Features converted to UniMorph 4.0          | 10,000                  | 1,000                  | 1,000 |
| Russian                                          | rus                     | Modified file format only                   | 10,000                  | 1,000                  | 1,000 |
| Belarusian                                       | bel                     | Provided by the SIGMORPHON shared task 2023 | 10,000                  | 1,000                  | 1,000 |

## Multilingual

| Name   | Languages                                                                                          | trn    | dev   | tst   |
| ------ | -------------------------------------------------------------------------------------------------- | ------ | ----- | ----- |
| slavic | pol, ces, slk, dsb, csb (West Slavic); Kashubian used for testing only                             | 40,000 | 4,000 | 4,509 |
| sla    | pol, ces, slk, dsb, csb, bel, rus, mkd (West, East, South Slavic); Kashubian used for testing only | 70,000 | 7,000 | 7,509 |
