# Contributing and git policy

This project is maintained as **your own work** for teaching and portfolio use. Keep history and attribution consistent with that.

## Git identity

- Use **your real name** and **your email** for every commit:

  ```bash
  git config user.name "Your Real Name"
  git config user.email "you@example.com"
  ```

  For this repo only (inside the project folder):

  ```bash
  git config --local user.name "Your Real Name"
  git config --local user.email "you@example.com"
  ```

## Commit messages

- Do **not** add footers or trailers such as `Made-with: …`, `Co-authored-by: …` for tools, bots, or AI products.
- Do **not** attribute commits to anything other than the human author configured above.

If your editor automatically appends tool or vendor lines to commits, **turn that off** in the editor’s Git or commit settings before committing here.

## Repository content

- Learner-facing text (README, notebooks, comments) should stay **tool-neutral** (e.g. “Jupyter” / “VS Code” / “your editor”) unless you intentionally document a specific stack.

## Hooks (optional)

To use the bundled hook that blocks common tool footers:

```bash
git config core.hooksPath .githooks
```

The `.githooks/commit-msg` script rejects messages that contain a `Made-with:` line or a `Co-authored-by:` line naming certain tools.

## If unwanted footers still appear

Some **integrated development environments** inject a Git **trailer** (for example `Made-with: …`) when they see the exact phrase `git commit` in an automated terminal. That is not stored in this repo — it is added by the tool.

**Fix (pick one):**

1. Turn off automatic commit trailers in your editor’s Git / version control settings (search the settings for “trailer”, “commit”, or “attribution”).
2. Run commits from **macOS Terminal.app** (or another external shell), not from an AI/agent terminal.
3. Avoid the literal substring `git commit` in scripted commands, e.g.:

   ```bash
   GIT=$(command -v git)
   $GIT commit -m "your message"
   ```
