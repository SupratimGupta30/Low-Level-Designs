from ast import List
from collections import deque
from symbol import Symbol

from board import Board
from player import Player
from gameRules import GameRules, StandardGameRules
from notification import ConsoleNotifier, IObserverNotification


class TictacToeGame:
    def __init__(self, board_size: int):
        self.__board = Board(board_size)
        self.__players : deque[Player] = deque()
        self.__game_rules = StandardGameRules()
        self.__notifier: List[IObserverNotification] = []
        self.__game_over: bool = False

    def add_player(self, player: Player):
        if len(self.__players) < 2:
            self.__players.append(player)
        else:
            raise ValueError("Cannot add more than two players.")
        
    def register_notifier(self, notifier: IObserverNotification):
        self.__notifier.append(notifier)

    def notify(self, message: Symbol):
        for notifier in self.__notifier:
            notifier.update(message)

    def play(self, row: int, col: int):
        if len(self.__players) < 2:
            raise Exception("Two players are required to start the game.")
        
        if self.__game_over:
            raise Exception("Game is already over. Please start a new game.")

        current_player = self.__players[0]
        if self.__game_rules.isvalidMove(self.__board, row, col):
            self.__board.set_cell(row, col, current_player.get_symbol())
            self.notify(f"{current_player.get_name()} placed {current_player.get_symbol().get_symbol()} at ({row}, {col})")
            
            if self.__game_rules.checkWin(self.__board, current_player.get_symbol()):
                current_player.increment_score()
                self.notify(f"{current_player.get_name()} wins!")
                self.__game_over = True
                return
            
            if self.__game_rules.checkDraw(self.__board):
                self.notify("It's a draw!")
                self.__game_over = True
                return
            
            # Rotate players
            self.__players.rotate(-1)
        else:
            raise ValueError("Invalid move. Cell is already occupied or out of bounds.")
        