# codealpha_tasks_1_hangman_game

# 2-in-1 Python Hangman Game 🎮

An interactive, dual-mode command-line Hangman game written in Python. Developed as part of the **CodeAlpha Python Programming Internship**, this project offers both traditional gameplay and an intelligent reverse-mode where the computer guesses your secret word using frequency analysis and dynamic candidate reduction.

---

## 🌟 Features

* **Mode 1: Classic Mode (You Guess)**
* The computer selects a random secret word from a vocabulary dataset.
* Interactive CLI feedback with life/mistake tracking.
* Robust input validation for duplicates, numbers, and invalid characters.


* **Mode 2: Reverse Mode (Computer Guesses)**
* Think of a secret word and let the computer do the solving!
* Uses letter frequency analysis to narrow down dictionary candidates efficiently.
* Adapts to user feedback on correctly guessed positions and revealed letters.


* **Clean & Modular Codebase**
* Object-oriented / modular Python design with edge-case handling.
* Clear terminal outputs and visual progress indicators.



---

## 📁 Repository Structure

```text
├── hangman.py          # Main application script (contains both game modes)
├── words.txt           # Dictionary/word list dataset for the game
├── README.md           # Project documentation

```

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.7+** installed on your system.
* No external third-party dependencies required (uses built-in standard libraries).

### Installation & Execution

1. **Clone the Repository:**
```bash
git clone https://github.com/your-username/hangman-2in1.git
cd hangman-2in1

```


2. **Run the Game:**
```bash
python hangman.py

```



---

## 💡 How to Play

Upon running the program, you will be prompted to select a game mode:

```text
========================================
       2-IN-1 HANGMAN GAME
========================================
1. You guess the computer's word
2. Computer guesses your word
========================================
Select mode (1 or 2): 

```

1. **Mode 1:** Enter single letters to guess the hidden word before running out of attempts.
2. **Mode 2:** Decide on a word, enter its length, and answer the computer's prompts (`y`/`n` and character indices) as it narrows down candidate words.

---

## 📺 Video Walkthrough

A complete line-by-line breakdown explaining the data structures, algorithms, and logical flow of the codebase is available here:

👉 **[Link to YouTube / Demo Video]**

---

## 🤝 Acknowledgments

This project was built during my internship at **CodeAlpha**. Special thanks to the team and community for supporting continuous learning and open-source development.
