from enum import Enum, auto
from tictactoegame import TicTacToeGame

class GameState(Enum):
    STANDARD = auto()

class TicTacToeGameFactory:
    @staticmethod
    def create_game(game_state: GameState, board_size: int):
        if game_state == GameState.STANDARD: 
            return TicTacToeGame(board_size)
        else:
            raise ValueError("Invalid game state")