# Judge Calibration

**Date:** _<dd/mm/yyyy>_
**Cohort member:** Rajavarman
**Data used:** MP1 Prompt Lab (Week 5 Graded Mini Project). I don't have a capstone `eval-run-001` yet, so this calibrates the same `gpt-4o` judge on MP1's 40 judged extractions (10 snippets × 4 prompt strategies).
**Sampled entries (10 of 40), stratified:** 6 clean (happy-path), 3 fuzzy (harder), 1 edge, spread across all 4 strategies.
**Note:** the MP1 judge gives **one** score (1-4) per entry, not three dimensions, so there are **10** scores to compare, not 30. Each disagreement moves the rate by 10%.

---

## The rubric (the judge's exact rubric from `mp1_prompt_lab.ipynb`, use this, nothing else)

- **4** - all three fields correct
- **3** - two of three correct, and no fabricated data
- **2** - one of three correct, or the model fabricated a field (e.g. invented a number where none was stated)
- **1** - none correct, or the output did not parse

The three fields are `company`, `role`, `years_experience_required`. Compare the **model output** with the **job posting** and the **gold answer**, the same way the judge did.

---

## The 10 entries to score

### 1. `j01-cot` (happy)

**Job posting:** Acme Corp is hiring a Senior Software Engineer to join our platform team. The ideal candidate has 5+ years of backend development experience and strong skills in Python and distributed systems.

**Gold answer:** `{"company": "Acme Corp", "role": "Senior Software Engineer", "years_experience_required": 5}`

**Model output:** `{"company": "Acme Corp", "role": "Senior Software Engineer", "years_experience_required": 5}`

### 2. `j02-zero_shot` (happy)

**Job posting:** We're looking for a Data Analyst at Northwind Ltd. Reporting to the Head of Analytics, you'll work with SQL, dashboards, and stakeholder requests. 2 years minimum experience preferred.

**Gold answer:** `{"company": "Northwind Ltd", "role": "Data Analyst", "years_experience_required": 2}`

**Model output:** `{"company": "Northwind Ltd.", "role": "Data Analyst", "years_experience_required": 2}`

### 3. `j02-few_shot` (happy)

**Job posting:** We're looking for a Data Analyst at Northwind Ltd. Reporting to the Head of Analytics, you'll work with SQL, dashboards, and stakeholder requests. 2 years minimum experience preferred.

**Gold answer:** `{"company": "Northwind Ltd", "role": "Data Analyst", "years_experience_required": 2}`

**Model output:** `{"company": "Northwind Ltd", "role": "Data Analyst", "years_experience_required": 2}`

### 4. `j03-structured` (happy)

**Job posting:** Globex International seeks a Product Manager - Growth. You'll own activation and onboarding metrics across our consumer apps. We're looking for someone with at least 4 years of product management experience in B2C contexts.

**Gold answer:** `{"company": "Globex International", "role": "Product Manager - Growth", "years_experience_required": 4}`

**Model output:** `{"company": "Globex International", "role": "Product Manager - Growth", "years_experience_required": 4}`

### 5. `j08-structured` (happy)

**Job posting:** Senior UX Researcher at Wonka Confectionery Ltd. You'll design and run user studies for our digital storefront. Five years of UX research experience or equivalent portfolio required.

**Gold answer:** `{"company": "Wonka Confectionery Ltd", "role": "Senior UX Researcher", "years_experience_required": 5}`

**Model output:** `{"company": "Wonka Confectionery Ltd.", "role": "Senior UX Researcher", "years_experience_required": 5}`

### 6. `j08-few_shot` (happy)

**Job posting:** Senior UX Researcher at Wonka Confectionery Ltd. You'll design and run user studies for our digital storefront. Five years of UX research experience or equivalent portfolio required.

**Gold answer:** `{"company": "Wonka Confectionery Ltd", "role": "Senior UX Researcher", "years_experience_required": 5}`

**Model output:** `{"company": "Wonka Confectionery Ltd", "role": "Senior UX Researcher", "years_experience_required": 5}`

### 7. `j04-zero_shot` (harder)

**Job posting:** Join Initech as a Lead DevOps Engineer. We need a builder, not a maintainer. Around 6 years of hands-on infrastructure work expected, ideally with AWS, Terraform, and modern CI/CD.

**Gold answer:** `{"company": "Initech", "role": "Lead DevOps Engineer", "years_experience_required": 6}`

**Model output:** `{"company": "Initech", "role": "Lead DevOps Engineer", "years_experience_required": 6}`

### 8. `j06-cot` (harder)

**Job posting:** Pied Piper Inc. has an opening for a Senior ML Engineer. Compression algorithms background a plus. We typically look for 7+ years in production ML and distributed systems, but exceptional candidates with less are welcome.

**Gold answer:** `{"company": "Pied Piper Inc.", "role": "Senior ML Engineer", "years_experience_required": 7}`

**Model output:** `{"company": "Pied Piper Inc.", "role": "Senior ML Engineer", "years_experience_required": 7}`

### 9. `j09-structured` (harder)

**Job posting:** Stark Industries: Cybersecurity Analyst (mid-level). Three to five years in a SOC environment or equivalent. Familiarity with SIEM tools, incident response runbooks, and basic threat modelling.

**Gold answer:** `{"company": "Stark Industries", "role": "Cybersecurity Analyst", "years_experience_required": 3}`

**Model output:** `{"company": "Stark Industries", "role": "Cybersecurity Analyst", "years_experience_required": 3}`

### 10. `j05-cot` (edge)

**Job posting:** Hooli is looking for a Junior Frontend Developer. Fresh grads welcome — no prior experience required. We care about curiosity and willingness to learn. JavaScript, React, and CSS fundamentals expected.

**Gold answer:** `{"company": "Hooli", "role": "Junior Frontend Developer", "years_experience_required": 0}`

**Model output:** `{"company": "Hooli", "role": "Junior Frontend Developer", "years_experience_required": null}`

---

## My scores (filled in blind, without looking at the judge)

Replace each `_` in the **My score** column with 1, 2, 3 or 4. Write one short reason in the note column.

| Entry | My score | One-line note |
|---|---|---|
| j01-cot | _ | _ |
| j02-zero_shot | _ | _ |
| j02-few_shot | _ | _ |
| j03-structured | _ | _ |
| j08-structured | _ | _ |
| j08-few_shot | _ | _ |
| j04-zero_shot | _ | _ |
| j06-cot | _ | _ |
| j09-structured | _ | _ |
| j05-cot | _ | _ |
