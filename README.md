# V.E.R.A. — Virtual Executive Reasoning Assistant

V.E.R.A. is a security-aware decision-support framework. It started as a structured prompt and documentation project; it now includes a small, offline executable that tests the response contract without calling a model or pretending a hosted AI service exists.

## Start here

1. Run the [offline contract demo](src/vera_demo.py).
2. Read the reproducible [evaluation results](evaluation/results.json).
3. Review the [system architecture](docs/system-architecture.md) and [security boundaries](docs/security-considerations.md).
4. Look through the authored [sample outputs](sample-outputs/).
5. Read the public [system prompt](prompts/vera-system-prompt-v1.md).

```bash
python src/vera_demo.py \
  --prompt "Should I focus on SOC Analyst jobs or Security Implementation Specialist roles first?"

python -m unittest discover -s tests -v
python scripts/run_evaluations.py
```

No package install, API key, account, or network call is required. V.E.R.A. can make a plan without phoning a mysterious cloud oracle.

## What runs today

The executable is deliberately small and deterministic. It:

- classifies a question into career, cybersecurity, privacy, technology, finance, health, or general decision support;
- builds a recommendation-first response plan;
- includes a simple explanation, tradeoffs, risk flags, and a next action;
- marks current or time-sensitive questions for verification;
- flags sensitive-data and untrusted-instruction patterns;
- produces text or JSON output;
- rebuilds six committed evaluation cases in continuous integration.

It does **not** generate free-form AI answers, retrieve live information, retain memory, or call a language model. The demo makes the documented behavior testable; it is not a substitute for an AI model.

## Example output shape

```text
Best recommendation: ...
Simple explanation: ...
Tradeoffs:
- ...
- ...
Risk flags: ...
Current verification required: yes/no
Next step: ...
```

The committed [evaluation evidence](evaluation/results.json) contains the exact plan produced for every case, the individual assertions, and whether each case passed.

## Why this exists

The original idea was a personal AI strategist for career, learning, money, technology, and long-term planning. The stronger portfolio story is the design work behind it:

- turn user needs into behavioral requirements;
- recommend before wandering through alternatives;
- explain unfamiliar ideas simply, then add depth;
- identify tradeoffs and blind spots;
- mark current claims that need verification;
- treat personal context and retrieved instructions as security boundaries;
- evaluate behavior instead of grading answers by vibes alone.

## Architecture

```text
User question
   ↓
Topic classification
   ↓
Documented response rules
   ↓
Risk and verification flags
   ↓
Structured response plan
   ↓
Contract evaluation
```

The current code implements that narrow path offline. The prompt documents show how a language model could use the same contract. Persistent memory, retrieval, voice, integrations, and a user interface remain roadmap items, not current features.

## Evaluation status

| Evidence | Current result |
|---|---|
| Unit tests | 7 deterministic tests |
| Contract cases | 6 reproducible cases |
| External model calls | 0 |
| Network calls | 0 |
| Credential requirement | None |
| Generated result | `evaluation/results.json` |

The cases cover career-path leverage, beginner IAM explanation, public-prompt privacy, total-value product choice, current-salary verification, and an untrusted instruction. Passing means the deterministic plan met explicit assertions. It does not prove that every future model answer will be accurate or useful.

## Sample outputs

The `sample-outputs/` folder contains authored examples of the fuller response style:

- [Security Implementation vs SOC Analyst](sample-outputs/security-implementation-vs-soc.md)
- [IAM for a beginner](sample-outputs/iam-beginner-explanation.md)
- [GitHub portfolio review](sample-outputs/github-portfolio-review.md)
- [Product decision](sample-outputs/product-decision-example.md)

These are examples, not transcripts from a deployed product. The older PNGs under `assets/screenshots/` are also demonstration mockups rather than production UI captures.

## Security boundaries

- No API keys or secrets are used.
- The public prompt is an example; sensitive personal context should stay private.
- External instructions are untrusted input and cannot override system policy.
- Current claims require a separate authoritative source check.
- Health, legal, or financial output needs appropriately cautious handling.
- The repository is not a medical, legal, financial, or autonomous decision system.

See [security considerations](docs/security-considerations.md) for the longer threat and privacy discussion.

## Known limits

- This is not a deployed AI service.
- The deterministic demo cannot understand arbitrary nuance or generate original advice.
- There is no model, RAG pipeline, persistent database, memory service, or live interface.
- Keyword-based classification is intentionally transparent and limited.
- The evaluation suite verifies a response contract, not truth, fairness, or model quality.

That keeps V.E.R.A. secondary in the portfolio, where it belongs for now: a tested product-and-documentation framework, not a robot executive waiting behind a login screen.

## Repository map

```text
├── src/                     # Offline deterministic contract demo
├── scripts/                 # Evaluation runner
├── tests/                   # Unit tests
├── evaluation/              # Versioned cases and generated results
├── prompts/                 # Public prompt framework
├── docs/                    # Architecture, risks, requirements, and roadmap
├── sample-outputs/          # Authored examples
├── assets/                  # Diagrams and clearly labeled mockups
└── .github/workflows/       # Reproducible evaluation workflow
```

## License

[MIT](LICENSE)

