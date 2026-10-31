# JARVIS Discovery Console

**A local-first, Iron-Man-inspired research and execution cockpit.** This is an original project and is not affiliated with Marvel or any fictional JARVIS implementation.

## What it does

- **Command interface:** rule-based prompts for idea intake, contradiction review, experiment design, opportunity ranking, and execution planning.
- **Project memory:** create and edit a small registry of research and software projects.
- **Hypothesis lab:** record claims, confidence, supporting evidence, counterevidence, and status; surface a limited set of possible opposing phrases for human review.
- **Experiment planner:** record a falsifiable hypothesis, baseline, metric, target, status, and observed result.
- **Opportunity engine:** rank user-entered opportunities using a transparent heuristic.
- **Portable data:** import/export a JSON backup.
- **Local-first:** user data is stored in browser `localStorage`; no API key or backend is needed.

## Open it

- GitHub source: [`jarvis/index.html`](./index.html)
- After GitHub Pages is enabled and its workflow succeeds, the app will be available at: `https://anurag1.github.io/Anurag1/` only if the repository's Pages configuration publishes this folder at the root. Otherwise use the URL shown in **Settings → Pages**. The included workflow publishes the `jarvis/` folder as the site root.
- You can also download `index.html` and open it in a modern browser.

## How the score works

Opportunity score (0–100):

```
30% potential value
+ 35% evidence strength
+ 20% speed to validate
+ 15% (5 - effort required)
```

Each input is a user-assigned integer from 0 to 5. This score is a sorting heuristic, not a financial forecast or evidence of market demand.

## Important limitations

This version is a **working static prototype**, not a connected autonomous AI agent. Command responses use deterministic local rules; the contradiction scan is a basic text heuristic and can miss real contradictions or flag unrelated claims. It does not connect to an LLM, GitHub API, email, microphone, camera, operating system, or other external services. It does not run background tasks.

Data is kept in the current browser profile and is not encrypted by this app. Clearing browser site data may erase it. Export backups regularly and do not store secrets or sensitive information.

## Development roadmap

1. Add browser-level regression tests for forms, persistence, import/export, and scoring.
2. Add a server-side model adapter with secrets stored server-side.
3. Replace phrase-based contradiction flags with an inspectable claim/evidence graph and testable rules.
4. Add reproducible evaluation against a simple baseline.
5. Consider authentication and encrypted remote persistence only when needed.

## License

MIT. See [LICENSE](./LICENSE).
