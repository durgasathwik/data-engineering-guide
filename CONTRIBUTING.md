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

Then uncomment or adjust the checks inside `.githooks/commit-msg` if you customize them.
