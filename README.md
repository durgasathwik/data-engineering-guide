# Data engineering guide — week 1

Python for my week 1 class. I’m not using pandas, just the standard library.

## Setup

```bash
git clone https://github.com/durgasathwik/data-engineering-guide.git
cd data-engineering-guide

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

If you use Jupyter, you can register this venv as a kernel:

```bash
python -m ipykernel install --user --name=de-guide-week1 --display-name="Python (DE Guide .venv)"
```

In VS Code, choose the interpreter from `.venv` so `pip install` goes to the right place.

## What’s here

The course plan is in `week1/HANDOUT.md` (I might keep that file local only).

So far I only added code for the first two days:

- `week1/exercises/day01.py` — day 1
- `week1/exercises/day02.py` — day 2 (reads `week1/data/notes.txt`)
- `week1/PROGRESS.md` — whatever I want to remember when I commit

Run:

```bash
python week1/exercises/day01.py
python week1/exercises/day02.py
```

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md)
