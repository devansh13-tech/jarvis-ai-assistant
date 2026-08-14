# 🤖 Jarvis AI Assistant

A Python-based voice assistant built step by step while learning Python, speech recognition, AI, and modular project architecture.

---

# 🚀 Jarvis Roadmap

## 🏆 Milestone 1 – Voice Assistant Basics ✅

### Goal
Build the basic speaking and greeting system for Jarvis.

### Completed
- Text-to-Speech using `pyttsx3`
- `speak()` function
- Time-based greetings
- Functions and code organization
- Basic Python control flow

### Days
- ✅ Day 1 – Text to Speech
- ✅ Day 2 – Speak Function
- ✅ Day 3 – Code Refactoring
- ✅ Day 4 – Greeting System
- ✅ Day 5 – Audio Recording

---

## 🏆 Milestone 2 – Speech Recognition & Listening ✅

### Goal
Teach Jarvis to listen to the user and convert speech into text.

### Completed
- Audio recording using `sounddevice`
- WAV file creation using `soundfile`
- Speech-to-Text using `faster-whisper`
- Error handling
- Continuous listening
- Wake-word detection
- Command listening

### Days
- ✅ Day 6 – Whisper Speech Recognition
- ✅ Day 7 – Error Handling
- ✅ Day 8 – Wake Word Detection
- ✅ Day 9 – Command Listening

---

## 🏆 Milestone 3 – Command Execution ✅

### Goal
Teach Jarvis to understand commands and perform actions.

### Completed
- Command processing
- General commands
- System commands
- Web commands
- Time and date commands
- Application launching
- Google search
- YouTube search
- GitHub search

---

## 🏆 Milestone 4 – Modular Architecture ✅

### Goal
Move from a single large Python file to a clean modular architecture.

### Completed
- Separated command handlers
- Created `commands/` package
- Created `core/` package
- Separated speaker functionality
- Separated general commands
- Separated system commands
- Separated web commands
- Improved project organization

---

## 🏆 Milestone 5 – Command Management & Reliability ✅

### Goal
Make Jarvis more reliable and easier to maintain.

### Completed
- Command cleaning
- Unknown-command handling
- Help command
- Exit/shutdown handling
- Error handling
- Reusable functions
- Cleaner command routing
- Continuous command-processing loop

---

## 🏆 Milestone 6 – Current Jarvis Core ✅

### Goal
Build the foundation required for a more intelligent and conversational Jarvis.

### Completed
- Modular command architecture
- General command handler
- System command handler
- Web command handler
- Conversation context foundation
- Central command processing
- Reusable speaker module
- Structured project folders

---

# 📅 Overall Progress

| Milestone | Status |
|---|---|
| Milestone 1 – Voice Assistant Basics | ✅ Completed |
| Milestone 2 – Speech Recognition & Listening | ✅ Completed |
| Milestone 3 – Command Execution | ✅ Completed |
| Milestone 4 – Modular Architecture | ✅ Completed |
| Milestone 5 – Command Management & Reliability | ✅ Completed |
| Milestone 6 – Current Jarvis Core | ✅ Completed |
| Milestone 7 | ⏳ Upcoming |
| Milestone 8 | ⏳ Upcoming |

### 🎯 Current Progress

**6 / 8 Milestones Completed — 75% 🚀**

---

# 🧩 Current Project Structure

```text
JARVIS/
│
├── assets/
│   └── output.wav
│
├── commands/
│   ├── __init__.py
│   ├── general.py
│   ├── system.py
│   └── web.py
│
├── core/
│   ├── __init__.py
│   ├── context.py
│   └── speaker.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt