# Data Model

## Opportunity

- id
- title
- audience
- problem
- evidence[]
- proposed_offer
- channels[]
- hypothesis
- status

## Content

- id
- opportunity_id
- platform
- text
- asset
- CTA
- tracking_url
- publication_status

## Experiment

- id
- hypothesis
- start_at
- end_at
- variants[]
- success_metric
- decision

## Event

- timestamp
- experiment_id
- content_id
- source
- event_type
- value

Event types:
- impression
- click
- lead
- purchase

## Revenue

Revenue is stored separately from vanity metrics so the system can calculate attributable economic outcomes.
