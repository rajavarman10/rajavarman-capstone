# MP1 -- Prompt Strategy Comparison Table

Model: `gpt-4o-mini` (extraction) - `gpt-4o` (judge) - temperature 0.0

## Overall comparison

| strategy   |   Accuracy (mean of 3) |   Parse rate |   Judge score (of 4) |   Total cost ($) |   Latency p50 (s) |
|:-----------|-----------------------:|-------------:|---------------------:|-----------------:|------------------:|
| zero_shot  |                    2.7 |            1 |                  3.9 |            0     |             1.379 |
| few_shot   |                    3   |            1 |                  4   |            0.001 |             1.377 |
| structured |                    2.8 |            1 |                  3.9 |            0.001 |             1.446 |
| cot        |                    2.7 |            1 |                  3.9 |            0.001 |             1.851 |

## By-field breakdown

| strategy   |   match_company |   match_role |   match_years_experience_required |
|:-----------|----------------:|-------------:|----------------------------------:|
| zero_shot  |             0.8 |            1 |                               0.9 |
| few_shot   |             1   |            1 |                               1   |
| structured |             0.9 |            1 |                               0.9 |
| cot        |             0.8 |            1 |                               0.9 |

## Failure pattern: j10 null-years trap

j10's snippet states no years requirement; gold `years_experience_required` is `null`. A strategy that fabricates a number here is hallucinating rather than extracting.

| strategy   | extracted                                                                                               | fabricated_years   |
|:-----------|:--------------------------------------------------------------------------------------------------------|:-------------------|
| zero_shot  | {'company': 'Cyberdyne Systems', 'role': 'AI/ML Research Scientist', 'years_experience_required': None} | False              |
| few_shot   | {'company': 'Cyberdyne Systems', 'role': 'AI/ML Research Scientist', 'years_experience_required': None} | False              |
| structured | {'company': 'Cyberdyne Systems', 'role': 'AI/ML Research Scientist', 'years_experience_required': None} | False              |
| cot        | {'company': 'Cyberdyne Systems', 'role': 'AI/ML Research Scientist', 'years_experience_required': None} | False              |