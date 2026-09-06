# Affiliate Opportunity Engine — Sandbox Prototype

A small, testable foundation for an affiliate-marketing opportunity pipeline.

## What it does

- scores opportunities using demand, commission, competition, content effort, and trust;
- ranks opportunities by a transparent formula;
- estimates expected revenue from traffic/conversion assumptions;
- performs a basic pre-publication check for an affiliate disclosure.

## Formula

`score = (demand × commission × trust) / (competition × content_effort)`

`expected_revenue = impressions × CTR × conversion_rate × commission`

These are hypotheses, not earnings guarantees.

## Current scope

This repository deliberately contains **no live affiliate credentials, merchant accounts, automated purchasing, or payout integration**. Real affiliate programs have their own terms and eligibility requirements.

Before publishing an endorsement, disclosures should be clear and conspicuous. The FTC specifically recommends clearly disclosing an affiliate relationship near the recommendation/link. See: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking

## Test

```bash
python test_engine.py
```

Expected result:

`ALL TESTS PASSED`

## Next engineering stages

1. Opportunity ingestion adapters.
2. Product/merchant data model.
3. Evidence/provenance checks.
4. Content-quality and disclosure gate.
5. Analytics event schema.
6. Experiment ranking and feedback loop.
7. Optional publishing adapters that comply with each platform's API and program terms.
