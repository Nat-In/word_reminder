<div align="center">
  <img src="images/architecture.png" width="500">
</div>

# Controller 
## 1. Controller Overview
The Controller is the central component responsible for the application's logic and for coordinating interactions between the UI Layer and the Data Layer.

Its main responsibility is to manage the application's behavior: determine which actions should be performed, in what order and how the application should respond to user events and operation results.

The Controller is not simply a mediator between other components. It contains its own decision-making logic and methods responsible for managing the application, its behaviour and its main processes.

To fulfil responsibilities, the Controller:
- handles events received from the UI Layer
- calls the necessary Data Layer methods to work with data
- manages the application's main processes, including word selection and the reminder cycle
- makes decisions based on operation results
- handles errors by analysing error information received from other components and determining how the application should respond
- sends commands to the UI Layer to display information and update the interface

The Controller does not directly perform database operations or handle the visual presentation of the interface. These responsibilities belong to the Data Layer and the UI Layer, respectively.

## 2. Controller Responsibilities
### 2.1 Application Startup
When the application starts, The Controller initiates the process of retrieving information about the database contents by calling the appropriate Data Layer method.

 The Data Layer returns the information needed by the Controller to determine the next steps:
- whether the database contains any words
- how many words have the status learn
- how many words have the status known

Based on the returned information, the Controller determines which startup scenario to follow.

#### Scenario 1: The database is empty
- The Controller instructs the UI Layer to display a message informing the user that the vocabulary is empty.
- After the message is displayed, the application terminates.

#### Scenario 2: Words with the learn status are available
- The Controller initiates the selection of a random word with the learn status.
- The reminder cycle starts.

#### Scenario 3: Only words with the known status are available
- The Controller instructs the UI Layer to display a message informing the user that no words with the learn status are available.
- The user is offered two options: Continue or Exit.
- If the user selects Continue, The Controller starts selecting random words with the known status.
- If the user selects Exit, the Controller terminates the application.

#### Separation of responsibilities:
- The Controller analyses the retrieved information and determines which startup scenario to follow.
- The Data Layer retrieves the required information from the database and returns the result.
- The UI Layer displays messages and passes the user's choice to the Controller.

### 2.2 Word Selection
The Controller is responsible for selecting words to display and determining which learning status has priority.

The word selection logic worcs as follows:
1. Before selecting each new word, the Controller checks whether words with the learn status are available.
2. If such words are available, the Controller requests a random word with the learn status from the Data Layer.
3. If no words with the learn status are available, the Controller offers the user two options:
   - **Continue** - continue displaying words with the known status.
   - **Exit** - terminate the application.
4. If the user selects Continue, the Controller requests a random word with the known status from the Data Layer.
5. If new words with the learn status become available, the Controller automatically prioritises them during the next word selection.

#### Additional Rules
- The Controller uses one general Data Layer method to retrieve a random word, passing the required status (learn or known) as an argument.
- If the application is already running in known mode, the absence of learn words must not trigger the same notification before every new cycle.
- The availability of learn words is checked before selecting each new word.
- If the application returns to a situation where no learn words are available, the user is offered the Continue or Exit options again.
- The appearance of new learn words does not interrupt the current reminder cycle. They are prioritised when the next word is selected.

#### Separation of Responsibilities
- The Controller determines which status should be used for word selection and manages the switching between selection modes.
- The Data Layer retrieves a random word with the required status and returns in to the Controller.
- The UI Layer displays notification and passes the user's choice the Controller.

### 2.3 Reminder Cycle Management
The Controller is responsible for managing the entire lifecycle of timers. This includes:
- starting timers
- storing timer identifiers so they can managed later
- cancelling timers when necessary
- handling timer completion and triggering the next action

It ensures that the reminder cycle follows the correct sequence and that scheduled actions are performed at the right time.

The reminder cycle consist of two intervals:
- **Display interval** - 15 minutes during which the word is displayed.
- **Break interval** - a 15 minute pause between words.

#### Cycle Sequence
The reminder cycle follows this sequence:
1. The Controller requests the next word from the Data Layer.
2. The Controllers sends the selected word to the UI Layer for display.
3. The Controller starts a 15 minute display timer.
4. When the display interval ends, the Controller:
   - instructs the UI Layer to close the reminder window if it is still open
   - starts a 15 minute break timer
5. When the break interval ends, the Controller starts selecting the next word.
6. After a new word is selected, the next cycle begins.

The timer repeats automatically while the application is raining.

#### Timer and Window Management
1. If the user clicks **Know**, the Controller stops the current word display timer, closes the window and immediately starts a 15 minute break timer.
2. If the user clicks **Learn**, the current timer continues running. The word remains displayed until the 15 minute display interval ends. After that, the break begins.
3. If the user minimises the window, the Controller does not stop the timer. When the display interval ends, a 15 minute break begins. After the break, the Controller selects a new word and the window with that word appears automatically.
4. If the user exits the application, the Controller cancels all active timers. No scheduled actions are performed after that.

#### Separation of Responsibilities
- The Controller manages the reminder cycle, timers and transitions between display and break intervals.
- The UI Layer displays and closes the reminder window when instructed by the Controller.
- The Data Layer provides the next word for display.

### 2.4 User Actions Handling
The Controller is responsible for handling user actions received from the UI Layer and determining what the application should do in response.

The main user actions are:
1. Meaning
   - The Controller receives an event when the user clicks the Meaning button.
   - The Controller instructs the UI Layer to display the meaning or description of the current word.
   - Viewing the meaning does not change the word's status or affect the current timer.

2. Know
   - The Controller receives an event when the user clicks the Know button.
   - The Controller initiates the process of changing the word's status to known.
   - The Controller then performs the required timer and window actions according to the Reminder Cycle Management logic.

3. Learn
   - The Controller receives an event when the user clicks the Learn button.
   - The Controller initiates the process of changing the word's status to learn.
   - The current display interval continues according to the Reminder Cycle Management logic.

4. Continue/Exit

If no words with the learn status are available when selecting the next word, the Controller receives the user's choice:
   - **Continue** - continues the application in known mode, displaying words with the known status.
   - **Exit** - starts the application shutdown process.

#### Separation of Responsibilities
- The UI Layer sends events related to user actions to the Controller.
- The Controller handles these events, determines what should happen next and coordinates the work of other components.
- The Data Layer performs data operations when requested by the Controller.

The UI Layer does not need to know how the Controller or Data Layer works internally. It only needs to know which visual actions to perform, such as displaying information or closing a window.

This separation makes the application easier to maintain. If the graphical library is replaced, only the UI Layer implementation should need to change. The Controller and Data Layer can remain unchanged, as long as the communication between the components stays the same.

### 2.5 Word Status Management

















 
















  
