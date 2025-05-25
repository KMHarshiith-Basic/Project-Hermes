# 🤖 CyberHunt Lite

A **terminal-based Python puzzle game** with a fun twist — you’re not solving alone. An unpredictable AI bot plays alongside you, randomly solving puzzles, sabotaging your moves, and turning your hacker dreams into a chaotic coding duel.

---

## 🚀 Project Overview

**CyberHunt Lite** is a simple, CLI-based game built in Python. The game presents the player with basic puzzles (like decoding ciphers or unscrambling words), while a lightweight AI bot takes alternate turns. The bot doesn't learn — it just causes chaos for fun.

---

## 🎯 Objectives

- Keep it **simple** — no GUI, no databases
- Use **pure Python** only
- Make the game **fun, fast, and playable**
- Ensure one teammate (newbie) can still contribute meaningfully

---

## 🕹️ Game Features

- 🎲 **Three Types of Puzzles**
  - **Caesar Cipher**: Decode a message encrypted using a simple shift
  - **Number Guessing**: Figure out a random number in a limited number of tries
  - **Word Scramble**: Unscramble jumbled letters into a meaningful word

- 🤖 **AI Bot**
  - Randomly "guesses" answers with a fixed chance of success
  - Occasionally blocks the player, skips a turn, or gives a fake clue
  - Very basic rule-based behavior (no learning or models)

- 🧠 **Turn-Based Gameplay**
  - You and the AI take turns solving the same puzzles
  - Scoreboard updates after each round
  - Play continues until all puzzles are done or a score limit is hit

---

## 📁 Folder Structure

```bash
CyberHuntLite/
├── main.py               # Game loop and core logic
├── puzzles.py            # All puzzle types (Caesar, Scramble, etc.)
├── ai_bot.py             # Simple AI bot logic
├── utils.py              # Helper functions (input validation, formatting)
├── requirements.txt      # Dependencies (optional)
├── README.md             # This file
└── /data
    └── wordlist.txt      # Word list for puzzles
