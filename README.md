# DE Guide — Week 1: Python Foundations for Data Engineering

Guided learning track: work through the notebooks and fill in the hands-on scripts with your tutor. Sample vendor CSVs live under `week1/data/sample/`.

## Setup

```bash
git clone https://github.com/durgasathwik/data-engineering-guide.git
cd data-engineering-guide

python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
python -m ipykernel install --user --name=de-guide-week1 --display-name="Python (DE Guide .venv)"
```

### Jupyter / notebook kernel

If your editor says notebooks need **`ipykernel`** or refuses to run cells:

1. **Do not** install packages into the system Python from Homebrew if you see **PEP 668 / externally-managed-environment** — use a **virtual environment** instead (the `.venv` above).
2. Select the project interpreter:
   - **VS Code / compatible editors:** Command Palette → **Python: Select Interpreter** → `.venv/bin/python` (or **Python (DE Guide .venv)** if you registered the kernel).
   - **Jupyter:** kernel picker → **`Python (DE Guide .venv)`** (kernelspec `de-guide-week1`).

Notebooks in this repo declare that kernelspec. Reload the notebook after changing the interpreter.

Optional [`.vscode/settings.json`](.vscode/settings.json) points at `.venv` for VS Code-based workflows.

## Week 1 objectives

- Python syntax and mental model for small pipeline utilities
- Collections, file I/O (CSV/JSON), exceptions, logging, modular scripts
- **stdlib only** for exercises (`csv`, `json`, `pathlib`, `logging`) — no pandas/polars

The **notebooks** are written for **beginners**: each topic explains ideas in plain language, adds short examples to run, then gives challenges with hints (not answer dumps).

## Layout

| Path | Purpose |
|------|---------|
| `week1/notebooks/` | Topics 1–5 — challenges and empty cells for your code |
| `week1/hands_on/` | Tasks 1–3 — reference CLI utilities (compare with your own attempts) |
| `week1/assignment/` | Vendor catalog ingestion — multi-file pipeline |
| `week1/data/sample/` | Five messy vendor CSVs for practice |
| `week1/interview_prep/week1_answers.md` | Six interview questions — write your answers |
| `week1/tests/` | `pytest week1/tests -v` |

**Guided learning:** work through the notebooks and interview doc first. The `hands_on/` and `assignment/` packages contain runnable reference code used by tests—reimplement or refactor them yourself, then diff against the repo when you are ready.

## Quick checks

Run from the **repository root** (the folder that contains `week1/`) so `week1` imports resolve.

```bash
python -m week1.assignment.run -i week1/data/sample -o week1/data/output/catalog.json

python week1/hands_on/task1_csv_to_json.py -i week1/data/sample/vendor_a.csv -o week1/data/output/task1.json
python week1/hands_on/task2_schema_validator.py -i week1/data/sample/vendor_a.csv
python week1/hands_on/task3_bad_record_logger.py -i week1/data/sample/vendor_b.csv -b week1/data/output/bad_rows.jsonl

pytest week1/tests -v
```

## Contributing / security

See [CONTRIBUTING.md](CONTRIBUTING.md) for git identity and commit guidelines. For forks and teams: use your normal review process, dependency updates, and any checks you rely on in CI.
