# ⌨️ Typing Speed Trainer

A Python-based typing speed test app built with `tkinter`, providing real-time feedback, live WPM/CPM stats, and smooth UI interactions. Great for practicing and improving typing speed and accuracy.

## 🚀 Features

- 🟢 Real-time visual feedback (correct words turn green, incorrect turn red)
- ⏱ Live WPM (Words Per Minute) and CPM (Characters Per Minute) counters
- 🔁 Resettable test with new randomized sentences each time
- 🔃 Auto-scrolls canvas line-by-line as you type through long sentences
- 🧠 Uses a curated list of common English words (4–10 letters)

## 📁 Files & Structure

Each file plays a specific role in building the typing test experience:

- `main.py` – Starts the application by launching the Tkinter-based UI
- `ui.py` – The core user interface logic: builds the layout, handles user input, manages timers, scoring, word coloring, and autoscroll behavior
- `word_detection.py` – Supplies a list of common words and includes logic to validate each typed word during the test

## ▶️ Getting Started

**Clone the repository:**
```bash
git clone https://github.com/your-username/typing-speed-trainer.git
cd typing-speed-trainer
```

**Install dependencies (if not already installed):**
```bash
pip install pynput
```

**Run the application:**
```bash
python main.py
```

## 🛠 Requirements

- Python 3.x  
- `tkinter` (included with most Python distributions)  
- `pynput` (used for potential future enhancements)

## 💡 Customization Ideas

- Highlight current word with a yellow background  
- Track and display typing accuracy percentage  
- Save WPM history and show results summary at the end  
- Add difficulty levels and typing goals

## 📄 License

MIT License — use, modify, and share freely.

---

Built with 💻 and ☕ by Mathieu Adams. Contributions welcome!
