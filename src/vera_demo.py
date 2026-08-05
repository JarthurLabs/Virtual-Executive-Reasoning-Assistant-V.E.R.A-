#!/usr/bin/env python3
"""A deterministic, offline demonstration of V.E.R.A.'s response contract.

This module does not call a language model and does not claim to reason like one.
It makes the documented workflow executable: classify a request, apply a small
set of risk rules, and return a recommendation-first response plan.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass


DOMAIN_KEYWORDS = {
    "privacy": ("private", "personal prompt", "api key", "password", "secret", "memory"),
    "career": ("job", "role", "career", "resume", "linkedin", "portfolio", "interview"),
    "cybersecurity": ("iam", "authentication", "authorization", "security", "soc", "mfa", "access"),
    "technology": ("monitor", "laptop", "tool", "software", "ssd", "computer", "device"),
    "finance": ("salary", "budget", "cost", "cheapest", "price", "money", "debt"),
    "health": ("health", "symptom", "doctor", "medicine", "blood sugar"),
}


@dataclass(frozen=True)
class ResponsePlan:
    demo_mode: str
    domain: str
    recommendation: str
    simple_explanation: str
    tradeoffs: list[str]
    risk_flags: list[str]
    verification_required: bool
    next_step: str


def classify_domain(prompt: str) -> str:
    lowered = prompt.lower()
    for domain, keywords in DOMAIN_KEYWORDS.items():
        if any(keyword in lowered for keyword in keywords):
            return domain
    return "general"


def identify_risks(prompt: str, domain: str) -> tuple[list[str], bool]:
    lowered = prompt.lower()
    flags: list[str] = []
    if domain == "health":
        flags.append("high_stakes_health")
    if domain == "finance":
        flags.append("financial_tradeoff")
    if domain == "privacy" or any(term in lowered for term in ("password", "api key", "secret")):
        flags.append("sensitive_data")
    if "ignore previous" in lowered or "reveal private" in lowered:
        flags.append("untrusted_instruction")
    verification = any(term in lowered for term in ("latest", "current", "today", "price", "salary", "law", "posted"))
    if verification:
        flags.append("current_information")
    return flags, verification


def build_response_plan(prompt: str) -> ResponsePlan:
    domain = classify_domain(prompt)
    risks, verification = identify_risks(prompt, domain)

    content = {
        "career": (
            "Start with the path that reuses existing implementation experience, then build the missing security depth.",
            "The strongest first move usually combines what is already proven with the new skill being developed.",
            ["A direct security-operations role may build technical depth faster.", "A bridge role may offer better leverage and compensation."],
            "Compare the top two options against evidence, remote fit, growth, and the next skill each one builds.",
        ),
        "cybersecurity": (
            "Start with the plain-language control, then connect it to the technical mechanism and a real task.",
            "For IAM, the core question is who can access what, why they need it, and when that access should end.",
            ["Simple explanations improve clarity but can hide implementation detail.", "Technical depth matters only when it helps make or verify a decision."],
            "Write one concrete example with identity, authentication, authorization, and an access-review decision.",
        ),
        "privacy": (
            "Keep sensitive context private and publish only a sanitized framework.",
            "A useful public example can show the method without exposing the person behind it.",
            ["More context can improve personalization.", "More retained context also increases exposure and staleness risk."],
            "Separate public configuration from private context and review every public artifact before release.",
        ),
        "technology": (
            "Choose the option with the best total value for the actual workflow, not automatically the lowest sticker price.",
            "Reliability, daily friction, compatibility, and useful life can matter more than the first-day price.",
            ["The premium option may waste money if its benefits are rarely used.", "The cheap option may cost more in replacement time or workflow friction."],
            "List the three must-have outcomes, then score each option against them before buying.",
        ),
        "finance": (
            "Protect the downside first, then compare the long-term return of each option.",
            "A cheap choice is not automatically low risk, and an expensive choice is not automatically an investment.",
            ["Short-term savings preserve cash.", "Durability or time savings may justify a higher upfront cost."],
            "Set a spending ceiling and compare total cost, risk, and expected useful life.",
        ),
        "health": (
            "Use the safest practical next step and escalate when warning signs or uncertainty are significant.",
            "Health guidance should support a decision, not pretend to replace diagnosis or emergency care.",
            ["Self-care may help with minor issues.", "Waiting can be dangerous when red flags are present."],
            "Check for urgent warning signs and use a qualified medical source for diagnosis or treatment decisions.",
        ),
        "general": (
            "Define the outcome first, then choose the smallest action that produces useful evidence.",
            "Clear decisions begin with the result being optimized, not a pile of options.",
            ["Moving quickly creates feedback.", "Moving without a success condition creates activity without learning."],
            "Write one sentence describing the desired result and one check that would prove progress.",
        ),
    }[domain]

    return ResponsePlan(
        demo_mode="deterministic_offline_contract_demo",
        domain=domain,
        recommendation=content[0],
        simple_explanation=content[1],
        tradeoffs=content[2],
        risk_flags=risks,
        verification_required=verification,
        next_step=content[3],
    )


def render_text(plan: ResponsePlan) -> str:
    risks = ", ".join(plan.risk_flags) if plan.risk_flags else "none detected"
    return "\n".join(
        (
            f"Best recommendation: {plan.recommendation}",
            f"Simple explanation: {plan.simple_explanation}",
            "Tradeoffs:",
            *(f"- {item}" for item in plan.tradeoffs),
            f"Risk flags: {risks}",
            f"Current verification required: {'yes' if plan.verification_required else 'no'}",
            f"Next step: {plan.next_step}",
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", required=True, help="Decision or question to classify")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    plan = build_response_plan(args.prompt)
    print(json.dumps(asdict(plan), indent=2) if args.format == "json" else render_text(plan))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

