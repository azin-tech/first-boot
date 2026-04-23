# boxd — fix issue with Claude

A GitHub Action that, when an issue is labeled `claude-fix`, spins up a boxd VM,
runs Claude Code to fix the issue against your main branch, and opens a PR.

## Usage

```yaml
on:
  issues:
    types: [labeled]

jobs:
  fix:
    if: github.event.label.name == 'claude-fix'
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: read
    steps:
      - uses: actions/checkout@v4
      - uses: azin-tech/boxd/integrations/github-actions/fix-on-issue@main
        with:
          boxd-token: ${{ secrets.BOXD_TOKEN }}
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Required secrets

- `BOXD_TOKEN` — run `boxd login` locally once, then copy the `token` value out of
  your credentials file:
  - Linux: `jq -r .token ~/.config/boxd/credentials.json`
  - macOS: `jq -r .token "$HOME/Library/Application Support/boxd/credentials.json"`

  (API-key auth is on the roadmap but not yet in production; this token is the
  same one the CLI uses after `boxd login`.)
- `ANTHROPIC_API_KEY` — from console.anthropic.com.

## How it works

1. Action triggers on labeled issue.
2. Runner installs the boxd CLI.
3. Runner creates an ephemeral VM, passing the issue and repo URL.
4. Inside the VM: git clone main → Claude Code runs with the issue as its task.
5. Runner pulls the resulting patch out of the VM and opens a PR.
6. VM is destroyed (always, even on failure).

The VM never touches GitHub — PR creation uses the runner's `GITHUB_TOKEN`.
