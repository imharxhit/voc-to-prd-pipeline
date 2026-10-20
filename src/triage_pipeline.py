#!/usr/bin/env python3
"""VoC-to-PRD Triage Pipeline: Links user friction clusters with MRR at risk and Gherkin specs."""
import json
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class BacklogSpec:
    cluster_id: str
    funnel_stage: str
    problem_statement: str
    affected_accounts: int
    mrr_at_risk_inr: float
    rice_score: float
    user_story: str
    gherkin_acceptance_criteria: List[str]


def build_prioritized_specs() -> List[BacklogSpec]:
    clusters = [
        {
            "cluster_id": "VOC-2026-014",
            "funnel_stage": "Checkout & Billing",
            "summary": "GST invoice download fails when billing address contains special characters",
            "reach": 420,
            "impact": 3.0,
            "confidence": 0.95,
            "effort_person_weeks": 1.5,
            "mrr_at_risk_inr": 1240000.0,
            "user_story": "As a B2B procurement manager, I want GST invoices to sanitize address punctuation automatically so that monthly input-tax-credit reconciliation never fails.",
            "gherkin": [
                "Given an active B2B account with '/' or '&' in billing_address_line_1",
                "When the user clicks 'Download Tax Invoice (PDF)' on the Order History page",
                "Then the invoice service escapes reserved characters and returns a valid GSTN-compliant PDF within 1500ms",
            ],
        }
    ]
    specs = []
    for c in clusters:
        rice = round((c["reach"] * c["impact"] * c["confidence"]) / c["effort_person_weeks"], 1)
        specs.append(
            BacklogSpec(
                cluster_id=c["cluster_id"],
                funnel_stage=c["funnel_stage"],
                problem_statement=c["summary"],
                affected_accounts=c["reach"],
                mrr_at_risk_inr=c["mrr_at_risk_inr"],
                rice_score=rice,
                user_story=c["user_story"],
                gherkin_acceptance_criteria=c["gherkin"],
            )
        )
    return specs


if __name__ == "__main__":
    print(json.dumps([asdict(s) for s in build_prioritized_specs()], indent=2))
