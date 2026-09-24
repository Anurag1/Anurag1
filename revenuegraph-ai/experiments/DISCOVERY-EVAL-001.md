# Discovery Evaluation 001

## Research question

Can an agent evaluation protocol distinguish ordinary task completion from discovery of a non-obvious, testable relationship?

## Protocol

For each problem:
1. Give the system the same task statement and permitted evidence.
2. Record the proposed relationship or hypothesis.
3. Require explicit supporting evidence.
4. Require a falsifiable test or verification procedure.
5. Have an independent evaluator score validity, novelty, and reproducibility.
6. Record cost and latency.

## Primary metrics

- Valid discovery rate
- Independently verified discovery rate
- Unsupported-claim rate
- Reproducibility rate
- Cost per verified discovery
- Median latency

## Comparison

Run at least two systems under the same evidence and tool constraints:
- Conventional answer-oriented baseline
- Discovery-oriented pipeline

Do not claim superiority unless the experiment is completed and the difference is statistically and practically meaningful.

## Initial hypothesis

A pipeline that explicitly represents assumptions, contradictions, relationships, and verification steps may surface different candidate relationships than a conventional answer-oriented baseline.

This is a hypothesis to test, not a result.

## Output schema

Each run should store:
- problem_id
- system_id
- hypothesis
- evidence_ids
- verification_method
- verdict
- novelty_score
- reproducibility_score
- latency_ms
- estimated_cost
- evaluator_notes
