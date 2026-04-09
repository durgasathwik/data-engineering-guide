# DE Guide — Week 1 (Python foundations)

This repo follows the **Week 1 course handout**: Python for data engineering beginners (stdlib only — no pandas).

## Setup

```bash
git clone https://github.com/durgasathwik/data-engineering-guide.git
cd data-engineering-guide

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Optional Jupyter kernel:

```bash
python -m ipykernel install --user --name=de-guide-week1 --display-name="Python (DE Guide .venv)"
```

Use the `**.venv` interpreter** in VS Code so installs work without PEP 668 errors.

## Week 1 layout

**7-day plan** in `week1/HANDOUT.md` (or your local copy if gitignored). The repo currently holds **Day 1–2** exercises only.


| Path                       | Purpose                                         |
| -------------------------- | ----------------------------------------------- |
| `week1/HANDOUT.md`         | 7-day schedule; Days 1–2 detailed, 3–7 outlined |
| `week1/data/notes.txt`     | For Day 2 (files)                               |
| `week1/exercises/day01.py` | Day 1 (topics 1–4)                              |
| `week1/exercises/day02.py` | Day 2 (topics 5–7)                              |
| `week1/PROGRESS.md`        | Your notes when you commit                      |


Use the standard library: `csv`, `json`, `logging`, `pathlib`, etc.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).