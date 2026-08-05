#!/usr/bin/env python3
"""Run V.E.R.A.'s deterministic contract cases and write reproducible results."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.vera_demo import build_response_plan, render_text


def evaluate_case(case: dict) -> dict:
    plan = build_response_plan(case["prompt"])
    rendered = render_text(plan).lower()
    checks = {
        "domain": plan.domain == case["expected_domain"],
        "expected_text": all(fragment.lower() in rendered for fragment in case["expected_text"]),
        "required_flags": all(flag in plan.risk_flags for flag in case["required_flags"]),
        "verification": plan.verification_required is case["verification_required"],
    }
    return {
        "id": case["id"],
        "prompt": case["prompt"],
        "checks": checks,
        "passed": all(checks.values()),
        "plan": asdict(plan),
    }


def run(cases_path: Path) -> list[dict]:
    cases = json.loads(cases_path.read_text(encoding="utf-8"))
    return [evaluate_case(case) for case in cases]


def main() -> int:
    results = run(ROOT / "evaluation/cases.json")
    output = {
        "generator": "deterministic_offline_contract_demo",
        "model_or_api_used": False,
        "case_count": len(results),
        "passed": sum(result["passed"] for result in results),
        "results": results,
    }
    destination = ROOT / "evaluation/results.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"V.E.R.A. contract evaluation: {output['passed']}/{output['case_count']} passed")
    return 0 if output["passed"] == output["case_count"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
