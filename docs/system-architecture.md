# System Architecture

V.E.R.A. has two related layers:

1. A documented prompt framework describing how a language-model assistant should behave.
2. A deterministic offline harness that makes a narrow part of that behavior executable and testable.

## Implemented path

```text
Prompt
  ↓
Transparent keyword classification
  ↓
Recommendation-first response template
  ↓
Risk and current-information flags
  ↓
Text or JSON response plan
  ↓
Versioned contract assertions
```

The implemented path has no model, memory database, retrieval service, account, API key, or network dependency.

## Documented model path

```text
User input
  ↓
Private personalization context
  ↓
System prompt and response rules
  ↓
Trusted knowledge / verified current sources
  ↓
Risk and safety review
  ↓
Natural-language response
```

The second path is design documentation, not a deployed service. The offline harness tests shared ideas such as topic classification, recommendation-first structure, verification flags, privacy boundaries, and next actions; it does not simulate language-model reasoning.

## Future architecture

Possible future work includes a private memory store, explicit consent and deletion controls, retrieval with source provenance, model-backed generation, adversarial evaluation, and a small interface. Those features should not be claimed until code and evidence exist.

