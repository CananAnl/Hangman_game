# Hangman

A classic word-guessing game where you reveal a hidden fruit name one
letter at a time before running out of attempts.

This project exists in two versions, built in order:

1. **`cli/`** — the original command-line version, written in Python.
   This was one of my first programming projects, where I focused on
   getting the core game logic right: tracking guessed letters,
   revealing correct letters, and counting failed attempts.
2. **`web/`** — a browser-playable version built afterward, with the
   same underlying logic reworked into a small interactive UI
   (vanilla HTML/CSS/JS, no build tools or dependencies).

Keeping both versions in the repo is intentional — it shows the
progression from a working script to a polished, shareable interface.

## Play it

**Web version (recommended):**
Open [`web/index.html`](./web/index.html) directly in your browser,
or play the live version here: `<add your GitHub Pages link here>`

**CLI version:**
```bash
python3 cli/hangman.py
```
Requires Python 3.9+ (uses `list[str]` type hints).

## How to play

- A random fruit name is chosen and shown as blank letter slots.
- Guess one letter at a time, using your keyboard or the on-screen keys.
- Correct guesses reveal every matching letter in the word.
- Wrong guesses count against your 6 total misses.
- Guess the full word before you run out of misses to win.

## Project structure

```
hangman-game/
├── README.md
├── LICENSE
├── .gitignore
├── cli/
│   └── hangman.py     # command-line version
└── web/
    └── index.html      # browser version (HTML/CSS/JS, single file)
```

## Possible next steps

- Add a word/category selector (fruits, animals, countries, etc.)
- Track win/loss stats across rounds using `localStorage`
- Add a difficulty setting that changes the number of allowed misses
- Write unit tests for the CLI version's guessing logic
