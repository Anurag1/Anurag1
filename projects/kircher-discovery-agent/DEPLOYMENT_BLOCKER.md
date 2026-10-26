# Deployment blockers

Checked 2026-10-26.

1. Lovable reports `is_published: true` and public audience for https://kircher-discovery-agent.lovable.app.
2. Source inspection of the Lovable project's `src/routes/index.tsx` showed the default blank-page placeholder and `data-lovable-blank-page-placeholder="REMOVE_THIS"`. This was an actual file read, not an assumption.
3. Lovable reported that the workspace was out of credits, preventing the repair prompt from running.
4. The model implementation in the project has a server-side `readOpenAIConfig()` reading `OPENAI_API_KEY` and `OPENAI_MODEL`, and has `getModelStatus`, `runLiveAnalysis`, and `runLiveModelTest` server functions.
5. `OPENAI_API_KEY` secret setup and real inference test were not completed/verified.
6. Dedicated GitHub repository `Anurag1/kircher-discovery-agent` has not been created; GitHub connector offered file write actions for existing repositories but no create-repository action. Python prototype and status docs are filed in `Anurag1/Anurag1/projects/kircher-discovery-agent/`.

## How to close blockers

- Add credits to the Lovable workspace or wait for credit allocation.
- Fix `src/routes/index.tsx` to mount the KDA interface and add `/setup` if missing; current available project file listing only showed `src/routes/index.tsx` and `src/routes/__root.tsx`.
- Run `npm test`, `npm run lint`, and `npm run build` in the app environment.
- Add API key only in project server secrets. Do not commit it.
- Use the UI's real-model test and require a successful response schema + nonce echo, then run a real research analysis.
- Redeploy, verify the homepage is not a placeholder, and synchronize all app source to a dedicated public repository.