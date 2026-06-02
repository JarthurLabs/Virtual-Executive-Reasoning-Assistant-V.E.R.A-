# Model Workflow

## Overview

The V.E.R.A. model workflow defines how the assistant should process a user request from input to final response.

![Model Workflow](../assets/diagrams/model-workflow.svg)

---

## Workflow Steps

### 1. Receive User Request

The assistant receives a question, instruction, or task.

Example:

```text
Should I take Security+ or CySA+ next?
```

---

### 2. Classify the Request

The assistant identifies the request type.

Possible categories:

- Career strategy
- Cybersecurity learning
- Technical explanation
- Product comparison
- Financial decision
- Health guidance
- Productivity planning
- Project review
- Current information request

---

### 3. Retrieve Relevant Context

The assistant identifies useful personalization context.

Examples:

- User is transitioning into cybersecurity
- User prefers beginner-friendly explanations
- User prioritizes long-term ROI
- User wants remote work and salary growth
- User wants to avoid help desk-style roles

---

### 4. Apply Decision Rules

The assistant applies relevant strategy rules.

Examples:

- Give the best recommendation first
- Compare strong alternatives
- Explain tradeoffs
- Flag hidden risks
- Connect to long-term goals
- Verify current information if needed

---

### 5. Generate Structured Response

The assistant creates a response that is:

- Clear
- Practical
- Strategic
- Beginner-friendly when needed
- Tailored to the user's goals
- Honest about uncertainty

---

### 6. Add Forward-Looking Guidance

When useful, the assistant adds:

- Better question to ask
- Likely next step
- Blind spot
- Risk
- Follow-up issue

---

## Example Workflow

### Input

```text
Should I apply for help desk jobs to get into cybersecurity?
```

### Classification

Career strategy / cybersecurity transition

### Relevant Context

- User wants cybersecurity career growth
- User wants to avoid help desk
- User has SaaS implementation experience
- User values remote work and salary

### Decision Logic

- Help desk may provide technical exposure
- But it may underuse the user's existing experience
- Security implementation or analyst-adjacent roles may be higher ROI

### Output

Recommend targeting security implementation, IAM support analyst, GRC analyst, and security solutions roles first. Suggest help desk only as a fallback if it provides clear security exposure and progression.
