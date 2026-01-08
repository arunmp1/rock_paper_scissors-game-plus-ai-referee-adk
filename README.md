# rock_paper_scissors-game-plus-ai-referee-adk
This project implements a minimal AI referee for a Rock–Paper–Scissors–Plus game as part of a placement assignment. The focus of the solution is on correctness, clear state management, and clean separation between conversational flow and game logic, rather than UI or advanced AI behavior.

The game state is maintained using a single Python dictionary that persists across turns. This state stores the current round number, maximum allowed rounds, scores for both the user and the bot, bomb usage for each player, and whether the game has ended. By keeping all state in one place and updating it explicitly through functions, the game flow remains predictable and easy to reason about, and no state is stored implicitly in prompts or user input.

The design follows an agent-and-tools approach. A Google ADK Agent is instantiated to represent the referee role and define the orchestration boundary of the system. All deterministic logic is implemented as explicit Python functions that act as tools. These tools handle move validation, round resolution, and game state updates. This ensures that rule enforcement and state mutation are kept separate from the conversational flow, which aligns with the intended agent design principles.

To keep the implementation simple and reliable, the game runs as a command-line application. The bot’s move selection is random rather than strategic, and tool execution is handled explicitly in the loop instead of being automatically driven by the agent. These tradeoffs were made to prioritize clarity, determinism, and compatibility with the available Google ADK Python package.

With more time, the project could be extended by adding a smarter bot strategy, more flexible natural language input handling, or a replay option after the game ends. The current version is intentionally minimal and focused on demonstrating correct logic, clean state modeling, and clear architectural separation.
