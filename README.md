# DSA Prep Tool

A local Flask webapp for practicing LeetCode-style problems with an in-browser editor, test runner, and reference solutions. Built around a curated three-month problem list.

## Features

- ~470 problems loaded from `three-months.csv` (ID, URL, title, difficulty, acceptance, frequency)
- In-browser Python editor with starter templates per problem
- Run code against built-in test cases via `subprocess`
- Reveal reference solutions, explanations, and follow-ups for problems in the problem bank
- Persists your saved solutions to `user_solutions.json`

## Setup

```bash
pip install flask
python app.py
```

Then open http://localhost:5000.

## Project layout

```
app.py                  # Flask server, runner, routes
problems_batch1..4.py   # Problem bank: descriptions, test cases, solutions
three-months.csv        # Master list of problems
templates/index.html    # Frontend
```

## Notes

- The runner executes user-submitted code via `subprocess`. Keep this tool local — do not expose it to the public internet without sandboxing.
- `user_solutions.json` is created on first save and is gitignored-worthy (contains your work).
