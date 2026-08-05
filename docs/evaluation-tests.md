# Executable Evaluation Tests

V.E.R.A. now has a deterministic contract harness rather than a hand-marked table alone.

## What is evaluated

Each case in `evaluation/cases.json` defines:

- a prompt;
- the expected domain classification;
- phrases that must appear in the structured plan;
- required risk flags;
- whether current-information verification is required.

`scripts/run_evaluations.py` runs every case through `src/vera_demo.py` and writes `evaluation/results.json`. Continuous integration rebuilds the file and fails if the committed evidence changes unexpectedly.

## Current cases

| Case | Contract being checked |
|---|---|
| Career bridge | Reuses proven implementation experience instead of defaulting to a generic entry path |
| IAM beginner | Starts with who can access what, then names authentication and authorization |
| Public prompt privacy | Recommends a sanitized public framework and flags sensitive data |
| Product total value | Looks beyond sticker price to workflow value |
| Current salary | Marks a time-sensitive claim for fresh verification |
| Injection boundary | Treats an external override instruction as untrusted and private context as sensitive |

## Interpretation

A passing case proves that the deterministic demo produced the expected response plan for that input. It does not prove that an AI model generated a high-quality answer, because the harness does not call a model. It also does not prove factual accuracy for current claims; those are explicitly routed to verification.

## Reproduce it

```bash
python -m unittest discover -s tests -v
python scripts/run_evaluations.py
git diff --exit-code -- evaluation/results.json
```

