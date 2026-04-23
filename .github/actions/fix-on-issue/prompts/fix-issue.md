You are fixing a GitHub issue in a cloned copy of the repo at `master`.
The working directory is `/home/boxd/first-boot`. It's already synced
to origin/master. You are user `boxd` (uid 1000), with `sudo` available.

The app's Python server is already running on http://localhost:3000 inside
this VM (live-forked from the golden), and Google Chrome is installed
at `/usr/bin/google-chrome`.

# The issue

Title: {{ISSUE_TITLE}}

Number: #{{ISSUE_NUMBER}}

Body:
```
{{ISSUE_BODY}}
```

# Your job

1. Read the codebase (`AGENTS.md`, `server.py`, `index.html`) and understand the issue.
2. **If this is a UI change** (edits to `index.html` or anything visible in the
   browser), capture a "before" screenshot first:
   ```bash
   mkdir -p .claude-screenshots
   /usr/bin/google-chrome --headless --disable-gpu --no-sandbox \
     --screenshot=.claude-screenshots/before.png --window-size=1280,800 \
     http://localhost:3000
   ```
3. Make the minimal change required to fix it.
4. **Always restart the Python server after any file change.** `server.py`
   reads `index.html` once at startup and caches it in memory, so even
   edits to `index.html` only take effect after a restart:
   ```bash
   pkill -f "python3 server.py" || true
   sleep 1
   (cd /home/boxd/first-boot && setsid nohup python3 server.py >/tmp/server.log 2>&1 </dev/null &)
   sleep 2
   curl -sf http://localhost:3000/ >/dev/null   # sanity
   ```
5. **For UI changes**, capture an "after" screenshot:
   ```bash
   /usr/bin/google-chrome --headless --disable-gpu --no-sandbox \
     --screenshot=.claude-screenshots/after.png --window-size=1280,800 \
     http://localhost:3000
   ```
6. Commit your changes on the current branch with a descriptive message.
   Use `git add -A && git commit -m "..."`. Subject line:
   `fix: <short description> (closes #{{ISSUE_NUMBER}})`.
7. Do NOT open a PR. Do NOT push. The caller will handle that.

If you need deeper browser inspection (clicking, console logs, network
requests), use the `chrome-devtools` MCP tools instead of headless CLI.

# Constraints

- Do not modify unrelated files.
- Keep the commit focused. Screenshots go in `.claude-screenshots/`.
- This repo has no test suite — verify correctness by hitting the server
  (`curl http://localhost:3000/`) and/or inspecting screenshots.
- If the issue is ambiguous or you cannot make progress, commit whatever
  partial work makes sense (with a clear message) and explain blockers.

When you're done (changes committed), print a final line: `DONE`.
