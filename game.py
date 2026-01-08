import random
from typing import Dict

game_state: Dict = {
    "round": 1,
    "max_rounds": 3,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False,
    "game_over": False
}

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

def validate_move(move: str, bomb_used: bool) -> Dict:
 
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return {"valid": False, "reason": "Invalid move"}

    if move == "bomb" and bomb_used:
        return {"valid": False, "reason": "Bomb already used"}

    return {"valid": True, "move": move}


def resolve_round(user_move: str, bot_move: str) -> str:
 
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"

    if bot_move == "bomb":
        return "bot"

    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    return "user" if rules[user_move] == bot_move else "bot"


def update_game_state(
    state: Dict,
    winner: str,
    user_move: str,
    bot_move: str
) -> Dict:
    
    if winner == "user":
        state["user_score"] += 1
    elif winner == "bot":
        state["bot_score"] += 1

    if user_move == "bomb":
        state["user_bomb_used"] = True

    if bot_move == "bomb":
        state["bot_bomb_used"] = True

    state["round"] += 1

    if state["round"] > state["max_rounds"]:
        state["game_over"] = True

    return state


def run_game():

    print("Rock-Paper-Scissors-Plus")
    print("Best of 3 rounds.")
    print("Moves: rock, paper, scissors, bomb (once per game).\n")

    global game_state

    while not game_state["game_over"]:
        print(f"--- Round {game_state['round']} ---")
        user_input = input("Your move: ")

        validation = validate_move(
            user_input,
            game_state["user_bomb_used"]
        )

        # Invalid input wastes the round
        if not validation["valid"]:
            print("Invalid input. Round wasted.\n")
            game_state["round"] += 1
            if game_state["round"] > game_state["max_rounds"]:
                game_state["game_over"] = True
            continue

        user_move = validation["move"]

        bot_choices = ["rock", "paper", "scissors"]
        if not game_state["bot_bomb_used"]:
            bot_choices.append("bomb")

        bot_move = random.choice(bot_choices)

        winner = resolve_round(user_move, bot_move)

        game_state = update_game_state(
            game_state,
            winner,
            user_move,
            bot_move
        )

        print(f"User played: {user_move}")
        print(f"Bot played: {bot_move}")
        print(f"Round result: {winner}\n")

    print("Game Over")
    print(f"Final Score → User: {game_state['user_score']} | Bot: {game_state['bot_score']}")

    if game_state["user_score"] > game_state["bot_score"]:
        print("Final Result: User Wins")
    elif game_state["bot_score"] > game_state["user_score"]:
        print("Final Result: Bot Wins")
    else:
        print("Final Result: Draw")


if __name__ == "__main__":
    run_game()
