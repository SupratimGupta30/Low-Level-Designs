from tictactoegame import TicTacToeGame
from player import Player
from symbol import Symbol
from creategame import GameState, TicTacToeGameFactory
from notification import ConsoleNotifier


def test_tictactoe_game():
    
    # Create a TicTacToe game with a 3x3 board
    size = int(input("Enter the board size (e.g., 3 for a 3x3 board): "))
    game = TicTacToeGameFactory.create_game(GameState.STANDARD, board_size=size)

    notifier = ConsoleNotifier()
    game.register_notifier(notifier)


    # Create two players
    player1 = Player(name="Alice", symbol=Symbol("X"))
    player2 = Player(name="Bob", symbol=Symbol("O"))

    # Add players to the game
    game.add_player(player1)
    game.add_player(player2)

    # Simulate a series of moves leading to a win for player1 (Alice)
    game.play()

if __name__ == "__main__":
    test_tictactoe_game()