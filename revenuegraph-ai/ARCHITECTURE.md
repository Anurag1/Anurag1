# Architecture

Observation -> Evidence -> Opportunity -> Hypothesis -> Content -> Distribution -> Conversion -> Measurement -> Learning

## Agents

### Scout
Finds observations, unanswered questions, recurring problems, and demand signals.

### Researcher
Collects evidence and provenance. Claims must remain traceable to their sources.

### Opportunity Agent
Maps an observation to an audience, problem, potential offer, and falsifiable commercial hypothesis.

### Content Agent
Produces platform-specific drafts from the validated research object.

### Publisher
Calls only authorized platform APIs. It does not bypass platform controls or automate prohibited behavior.

### Conversion Agent
Creates or updates the experiment landing page, CTA, and attribution parameters.

### Analytics Agent
Records impressions, clicks, leads, conversions, and revenue.

### Experiment Agent
Compares hypotheses and selects the next test based on observed evidence.

## Core loop

graph -> hypothesis -> experiment -> market response -> graph

The system should reject an opportunity when evidence or conversion data is weak.
