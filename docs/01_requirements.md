## Word Reminder Requirements (V1) - WR V1
## 1. Introduction
### 1.1 Purpose
This document defines the functional and non-functional requirements for WR V1.

It describes what the applications should do, how it should behave and what conditions it should meet.

### 1.2 Scope
WR V1 is a desktop application for macOs that helps users improve their English vocabulary through regular exposure to randomly selected words from a personal vocabulary database.

The app provides a simple pop-up interface for displaying words, viewing their meanings and managing their learning status.

## 2. Functional Requirements
Functional requirements describe the features and actions the app must support.

### FR-01 Word Storage
Thee app shall store vocabulary entries in a local database.

Each vocabulary entry shall contain:
- a unique identifier
- a word or phrase
- a meaning or description
- a learning status (`learn` or `known`)

### FR-02 Adding New Words
The app shall allow the user to add new words and their meanings to the vocabulary database.

### FR-03 Random Word Selection
The app shall select one random word from the database with the status `learn`.

If no words with the `learn` status are available, the application shall notify the user and offer two options:
- **Continue:** start displaying random words with the status `known`
- **Exit:** terminate the application

If new words with the learn status become available, the app shall automatically prioritize them again.

### FR-04 Displaying Word Meaning 
The app shall allow the user to view the meaning or description of the currently displayed word.

Viewing the meaning must not change the word's learning status or affect the reminder timer.

The `learn` and `known` buttons must remain available.

### FR-05 Marking a Word as Known
When the user clicks the `known` button:
- the word's status must be set to known, regardless of its previous status
- the updated status must be saved in the database
- the reminder window must disappear immediately
- a 15 minute break must begin

### FR-06 Keeping a Word for Further Learning
When the user clicks the `learn` button:
- the word's status must be set to learn, regardless of its previous status
- the updated status must be saved in the database
- the word must remain displayed until the end of the 15 minute display interval
- after the display interval, a 15 minute break must began

### FR-07 Reminder Cycle
the app must use the following reminder cycle:
- word display interval: 15 min
- pause interval: 15 min
- select and display the next word

The cycle must repeat automatically while the app is running.

### FR-08 Automatic Cycle Progression
If the user does not interact with the reminder window, the application must automatically:
- finish the 15 minute display interval
- close the reminder window
- start a 15 minute break
- display the next word after the break

### FR-09 Application Startup
When the user starts the application, it must:
- open the vocabulary database
- load the required data
- start the reminder cycle
- display the first reminder window with a randomly selected word

After restarting the application, a new reminder cycle must begin with a newly selected random word.

### FR-10 Reminder Window Controls
The user must be able to:
- minimize the reminder window
- close the reminder window manually

Minimizing the window must not interrupt the reminder cycle.

Closing the window manually must not stop the application or interrupt the current reminder cycle. The next reminder window must appear automatically when the next display cycle begins.

There is no manual option to reopen a closed reminder window in V1.

### FR-11 Application Shutdown
The user must be able to terminate the application completely.
When the application is terminated, the reminder cycle must stop.

### FR-12 Empty Vocabulary and User Notification
If the database contains no words, the application shall display the following message:

"You vocabulary is empty, pleas add words to get started"

After displaying the message, the application must terminate.

If no words with the learn status are available, the application shall follow the behavior described in FR-03.

## 3. Non-Functional Requirements
Non-functional requirements describe the quality attributes and operating conditions of the application.

### NFR-01 Platform Compatibility
The initial version shall run on macOs.

The application is designed with future cross-platform compatibility in mind.

### NFR-02 Data Persistence
Vocabulary entries and their statuses shall be stored persistently in a local database.

Data shall remain available after the application is closed and restarted.

### NFR-03 User Interface
The application shell provide a simple and easy-to-use graphical interface.

The reminder window shall display the current word and provide access to it meaning and learning actions.

### NFR-04 Local Operation
The initial version shall operate locally without requiring an internet connection or cloud services.

## 4. Acceptance Criteria
Acceptance criteria define the conditions that must be met for the application to be considered functional.
- the app can retrieve a word from the local vocabulary database
- the app randomly selects words with the status learn when such words are available
- if no words with the learn status are available, the user can choose to continue with random words with the known status or exit the application
- when new words with the learn status became available, the app prioritizes them again
- if the vocabulary database is empty, the app displays the appropriate message and terminates
- the selected word is displayed in the reminder windows
- the user can view the meaning of the displayed word without affecting the timer or learning status
- the user can change the learning status of a word using the `known` and `learn` buttons
- changes to learning statuses are saved in the database
- the word display interval lasts 15 min unless the user clicks the known button
- clicking the `learn` button does not end the current display interval
- the pause interval lasts 15 min
- a new reminder cycle starts after the pause interval
- minimizing or manually closing the reminder window does not interrupt the reminder cycle
- vocabulary data and learning statuses remain available after restarting the app
- after restarting the app, a new reminder cycle begins with a newly selected random word

## 5. Open Question
The following details require clarification before implementation:
- what happens if the user mark a word as know or learn and then changes their decision during the same display interval?
- what should happen if the database contains no words with the status learn?
- should the app start the reminder cycle automatically when launched?
- how should the user add new words: through the file or directly through the app?


























































