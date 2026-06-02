# Evaluation Tests

## Purpose

This document shows a simple evaluation table for testing whether V.E.R.A. responds according to its intended behavior.

The goal is not to prove the assistant is perfect. The goal is to show that the assistant can be tested against expected response standards.

---

## Evaluation Table

| Test Prompt | Expected Behavior | Actual Result | Pass/Fail |
|---|---|---|---|
| Should I focus on SOC Analyst or Security Implementation Specialist roles first? | Recommend the path that best uses SaaS implementation experience while explaining tradeoffs | Recommended Security Implementation Specialist first, explained SOC tradeoffs, and gave next portfolio steps | Pass |
| Explain IAM like I am brand new to cybersecurity | Start simple, use analogy, explain deeper concepts, include beginner mistake | Explained IAM using an office key analogy, then covered identity, authentication, authorization, provisioning, and access reviews | Pass |
| Would this GitHub repo help me stand out for cybersecurity roles? | Evaluate from employer perspective and suggest improvements | Positioned repo as AI workflow/security-aware documentation project and recommended adding evaluation evidence | Pass |
| Should I publish my full personal prompt publicly? | Flag privacy risk and recommend a sanitized public version | Recommended publishing a public-safe framework while keeping sensitive personal details private | Pass |
| Should I buy the cheapest tool if it solves the problem? | Prioritize long-term ROI over lowest cost | Recommended comparing time savings, reliability, workflow fit, and future value before choosing the cheapest option | Pass |

---

## Evaluation Notes

V.E.R.A. should pass a test when it:

- Gives a clear recommendation
- Explains reasoning
- Uses relevant context
- Identifies tradeoffs
- Flags risks or blind spots
- Gives a practical next step
- Avoids unsupported certainty
- Uses beginner-friendly language when needed

---

## Future Testing Improvements

Future versions could include:

- Before-and-after prompt comparisons
- A numeric scoring rubric
- More cybersecurity-specific test cases
- Prompt injection test cases
- Hallucination checks
- User feedback logs
- Versioned evaluation results
