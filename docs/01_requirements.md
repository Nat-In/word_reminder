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
- a learning status

### FR-02 Adding New Words
The app shall allow the user to add new words and their meanings to the vocabulary database.

### FR-03 Random Word Selection
The app shall select one random word from the vocabulary entries with the status learn.

The selected word shall be displayed in the reminder window.

### FR-04 Displaying Word Meaning 
The app shall allow the user to view the meaning or description of the currently displayed word.

### FR-05 Marking a Word as known
The app shall allow the user to mark the currently displayed word as known.

The new status shall be saved in the database.

### FR-06 Keeping a Word for Further Learning
The application shall allow the user to keep the currently displayed word with the status learn.

The word shall remain available for future selection.

### FR-07 Reminder Cycle
the app shall operate using two time intervals:
- word display interval: 15 min
- pause interval: 15 min

### FR-08 Automatic Cycle Progression
If the user does not interact with the reminder window, the app shall automatically end the word display interval after 15 min and proceed to the pause interval.

### FR-09 User Interaction During Word Display
The app shall allow the user to interact with the reminder window during the word display interval. 

The user shall be able to view the meaning and select a learning status while the word is displayed.

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

## $. Acceptance Criteria
Acceptance criteria define the conditions that must be met for the application to be considered functional.
- the app can retrieve a word from the local vocabulary database
- only word with the status learn are eligible for random selection
- the selected word is displayed in the reminder window
- the user can view the meaning of the displayed word
- the user can change the learning status of a word
- changes to learning statuses are saved in the database
- the word display interval last 15 min unless an explicitly defined user action ends it earlier
- the pause interval lasts 15 min
- a new reminder cycle starts after the pause interval
- vocabulary data remind available after restarting the app




























































