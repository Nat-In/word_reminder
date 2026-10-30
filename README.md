word_reminder/
│
├── app.py                 - main startup file
├── logger.py              - logging settings
├── config.py              - project setings 
│
├── word_loader.py         - loading words from yamal
├── word_window.py         - popup reminder window
├── random_word.py         - get a random word to disply           
│
├── add_words.yaml         - file with added words
├── app.log                - application operation records
│
├── db/                    - entire related to the db
│   ├── create_db.py
│   └── wordsdb.sqlite     - are created automatically
│
├── requirements.txt       - external Python libraries
├── README.md
└── venv/


# Word Reminder — english vocabulary trainer (V1)
A simple Python application for macOS that helps memorize English words by showing small pop-up notes on the screen at regular intervals.  
To display one random English word every 15 minutes in a small window that stays on top of other windows.  
The user can view the meaning, mark the word as known, or leave it for further learning.

# installation 
This section explains how a user can set up the project on their computer.
1. *clone the repository*
  download project from GitHub
    bash -> git clone <https://github.com/Nat-In/word_reminder.git> 
    bash -> cd word_reminder
2. *create a virtual environment* (optional)
  helps to separate project dependencies from system Python
    bash -> python3 -m venv venv
2.2. *activate the environment*
    bash -> source venv/bin/activate   # for macOS/Linux
    bash -> venv\Scripts\activate      # for Windows
3. *install the dependencies*
  installs required Python libraries listed in requirements.txt
    bash -> pip install -r requirements.txt
4. *run the application*
    bash -> python app.py

# usage
1. run the app:  
  bash python app.py
2. a small pop-up appears with a random word from the "learn" list
3. click one of the buttons:
  - show meaning -> reveal full text and examples
  - know -> mark as known and close window
  - learn -> keep in learning list and close window
4. the app waits 15 minutes, then shows the next random word
5. adding new words from the add_words.yaml file 

# config.py
All project settings. It store path to files, reminder settings, UI settings, default values. To call function with 
- from config import ....

# logger.py
All processes will be recorded in file /app.log/

# pop-up reminder window
- show every 15min, stays active for 15min
- displays one random word
- on top of other windows
- buttons:
  'meaning' -> description
  'know' -> mark, close the window, start 15min pause
  'learn' -> keep as learning, close the window, start 15min pause
- if no buttons is pressed, the window stay visible for 15min and closes automatically for a pause
15min show -> 15min pause -> repeat
- new random word appears each cycle

# data structure
all words are stored in one SQLite database file

| Field        | Type     | Description |
|---------------|----------|-------------|
| 'id'          | INTEGER  | unique identifier (primary key)
| 'word'        | TEXT     | english word or phrase
| 'details'     | TEXT     | description with meaning
| 'status'      | TEXT     | "learn" or "know"
| 'created_at'  | DATETIME | when the word was added

# tech stack
  *language* - Python 3 
  *database* - SQLite
  *UI Library* - Tkinter (for pop-up windows)
  *OS* - macOS 

# roadmap


# author
Project by Nat_In
  - a personal tool for learning English vocabulary through repetition and self-made notes.
  It's created for studying and practicing Python. A hands-on development project. 