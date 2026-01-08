# rock_paper_scissors-game-plus-ai-referee-adk
This repository contains a simple AI referee for a Rock–Paper–Scissors–Plus game, developed as part of a placement assignment. The goal of the project is not to build a polished game, but to demonstrate clean reasoning, proper state handling, and a clear separation between conversational flow and game logic.

The game is played between a user and a bot and runs for a maximum of three rounds. The allowed moves are rock, paper, scissors, and bomb, where bomb can be used only once per player during the entire game. A bomb beats all other moves, bomb versus bomb results in a draw, and any invalid input wastes the round. After three rounds, the game ends automatically and a final result is displayed.

The implementation follows an agent-style approach where the conversational flow is separated from the actual game logic. User input is interpreted at a high level, while all rule enforcement and state updates are handled through explicit Python functions. This ensures that the game behaves deterministically and that the rules are enforced consistently, without relying on prompts or hidden state.

Game state is stored in a single Python dictionary that persists across turns. It tracks the current round, scores for both the user and the bot, bomb usage, and whether the game has ended. State updates happen only through dedicated functions, which makes the flow of the game easy to understand and reason about.

The project is implemented as a command-line application, which is sufficient for the scope of this assignment. The bot’s moves are chosen randomly, keeping the focus on correctness and architecture rather than strategy or UI complexity.

To run the game, ensure that Python 3 is installed and execute the script using python rps_plus_referee.py. The game will guide you through each round and display the outcome clearly.

With additional time, this project could be extended with a smarter bot strategy, improved natural language input handling, or replay functionality. However, the current version is intentionally kept minimal to highlight core engineering principles such as state modeling, tool-based logic, and clean separation of concerns.
