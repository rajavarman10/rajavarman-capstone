# MP1 — Reflection

*Rajavarman · Week 5 Graded Mini Project*

> **How to use this template:** run `mp1_prompt_lab.ipynb` end-to-end first, so `mp1_comparison.md` and the
> notebook's failure-pattern cells hold real numbers. Each section below has the question, guidance on what a
> strong answer draws on, and a `>` blockquote with a starting point — replace the bracketed parts with your
> actual numbers and observations before submitting. Target 300–500 words total; don't pad.

## 1. Which strategy won, and on what dimension?

Look at the `summary` table (accuracy, parse rate, judge score, cost, latency). It's rare for one strategy to
win on every dimension — name the one that won on accuracy, and note if a different one won on cost or
latency instead.

> few_shot had the highest mean accuracy (3.0/3) and judge score (4.0/4), tied for the fastest latency (1.38s) with zero_shot, and cost was negligible across all four (under a cent for 10 calls each). Unlike a typical accuracy-vs-cost tradeoff, few_shot won outright here with no real downside.

## 2. What surprised you?

Good sources for this: the j10 null-years check (did any strategy fabricate a number?), the by-field
breakdown (was one field consistently weaker?), disagreements between accuracy and judge score, or a specific
snippet that tripped up a strategy you expected to do well.

What surprised me most: every strategy — including plain zero-shot — correctly returned null for j10 instead of fabricating a number, which the course FAQ specifically calls out as the common failure mode. This suggests the null-safety came from the explicit "don't guess" instruction shared across all four prompts, not from the prompting technique itself — the strategies differed in accuracy on the other fields, but not on this guardrail. Also notable: chain-of-thought had the highest latency (1.85s vs ~1.4s for the others) without any accuracy benefit — the extra reasoning added time cost but no measurable payoff on this task

## 3. For your capstone domain, which strategy would you reach for first?

My capstone project is a RAG (Retrieval-Augmented Generation) system over the banking and NSE (National Stock Exchange) domain — grounding answers in retrieved regulatory circulars, banking policy documents, and exchange filings rather than the model's own memory. That's a structured-extraction problem too: pulling clean fields (circular reference numbers, effective dates, affected instruments, penalty clauses) out of retrieved text so the system can cite and reason over them precisely.

Given few-shot won on accuracy, judge score, and latency in MP1 with no real cost penalty, I'd reach for it first for the capstone's extraction step. The null-safety finding matters even more here than in MP1: in a banking/regulatory context, a system that fabricates a compliance date or penalty amount when the source document doesn't actually state one is far more dangerous than a system that correctly says "not found" — so I'd carry over the same explicit "don't guess, return null" instruction that made every MP1 strategy avoid the j10 trap.
*(Replace this section freely if you'd rather ground it in your MP1 numbers only, or in a different capstone
domain — this is just a starting point.)*

## 4. If you had another day, what would you try next?

Options worth naming: more snippets (to reduce noise in the 10-sample averages), a different model for
comparison (explicitly a stretch goal per the FAQ, not to mix into the main 4-strategy comparison), running
the LLM judge 3× and taking the median (the FAQ notes judge variance is a real, worth-noting issue), or a
5th "minimal baseline" strategy.

I'd dig into why zero-shot and CoT scored lower specifically on the company field (0.8 match rate vs few_shot's 1.0) — pulling the actual mismatched extractions would show whether it's a formatting issue (e.g. "Inc." vs "Inc") or a real extraction miss. I'd also run the LLM judge 3× and take the median, since the FAQ notes judge-score variance is a real, worth-noting issue I didn't check for here.
