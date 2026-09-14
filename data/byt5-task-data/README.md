# ByT5: Fine-tuning data

ByT5 accepts data in .tsv or .json format.

## File naming:<language></language>

```
{languageCode}{languageContext}_{dataSplit}
```

## Language code: monolingual data

<table>
<tr><th></th><th>Language code</th><th>Language</th><th>trn</th><th>dev</th><th>tst</th></tr>
<tr><td rowspan="5">West Slavic</td><td>ces</td><td>Czech</td><td>10,000</td><td>1,000</td><td>1,000</td></tr>
<tr><td>csb</td><td>Kashubian</td><td>/</td><td>/</td><td>509</td></tr>
<tr><td>dsb</td><td>Lower Sorbian</td><td>10,000</td><td>1,000</td><td>1,000</td></tr>
<tr><td>pol</td><td>Polish</td><td>10,000</td><td>1,000</td><td>1,000</td></tr>
<tr><td>slk</td><td>Slovak</td><td>10,000</td><td>1,000</td><td>1,000</td></tr>
<tr><td rowspan="3">East & South Slavic</td><td>bel</td><td>Belarusian</td><td>10,000</td><td>1,000</td><td>1,000</td></tr>
<tr><td>mkd</td><td>Macedonian</td><td>10,000</td><td>1,000</td><td>1,000</td></tr>
<tr><td>rus</td><td>Russian</td><td>10,000</td><td>1,000</td><td>1,000</td></tr>
</table>

## Language code: multilingual data

<table>
<tr><th></th><th>Language code</th><th>Language</th><th>trn</th><th>dev</th><th>tst</th></tr>
<tr><td>West Slavic</td><td>slavic</td><td>Czech, Lower Sorbian, Polish, Slovak</td><td>40,000</td><td>4,000</td><td>/</td></tr>
<tr><td>West & East & South Slavic</td><td>slavic-dist</td><td>Czech, Lower Sorbian, Polish, Slovak, Belarusian, Macedonian, Russian</td><td>70,000</td><td>7,000</td><td>/</td></tr>
</table>

### Language code: Synthetic Kashubian data

<table>
<tr><th></th><th>Language code</th><th>Language</th><th>trn</th><th>dev</th><th>tst</th></tr>
<tr><td>Kashubian (synthetic)</td><td>csb-gemini</td><td>Kashubian (synthetic)</td><td>10,000 (synthetic)</td><td>1,000 (synthetic)</td><td>/</td></tr>
<tr><td>Kashubian + Polish</td><td>csb-pol</td><td>Kashubian (synthetic) + Polish</td><td>10,000 (synthetic) + 10,000</td><td>1,000 (synthetic) + 1,000</td><td>/</td></tr>
</table>

## Language context: Code, word, family, or none

| Language context | Description                                     | e.g. for Polish      |
| ---------------- | ----------------------------------------------- | --------------------- |
| /                | No language context given                       | /                     |
| -lang-code       | Language code                                   | "pol"                 |
| -lang-word       | Language name as word                           | "Polish"              |
| -family          | Language Family                                 | "Slavic"              |
| -word-or-family  | 50% Language name as word & 50% language family | "Polish" / "Slavic" |
