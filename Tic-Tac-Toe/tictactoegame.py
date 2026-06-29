from ast import List
from collections import deque
from symbol import Symbol

from board import Board
from player import Player
from gameRules import GameRules, StandardGameRules
from notification import ConsoleNotifier, IObserverNotification


class TicTacToeGame:
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

    def play(self):
        if len(self.__players) < 2:
            raise Exception("Two players are required to start the game.")
        
        self.notify("Game started! Players: {} ({}), {} ({})".format(
            self.__players[0].get_name(), self.__players[0].get_symbol().get_symbol(),
            self.__players[1].get_name(), self.__players[1].get_symbol().get_symbol()
        ))
        
        while not self.__game_over:
            self.__board.display_board()
            current_player = self.__players[0]
            print(f"{current_player.get_name()}'s turn ({current_player.get_symbol().get_symbol()})")
            
            try:
                row = int(input("Enter row (0-indexed): "))
                col = int(input("Enter column (0-indexed): "))
                if self.__game_rules.isvalidMove(self.__board, row, col):
                    #print(current_player.get_symbol().get_symbol())
                    self.__board.set_cell(row, col, current_player.get_symbol())
                    self.notify(f"{current_player.get_name()} placed {current_player.get_symbol().get_symbol()} at ({row}, {col})")
                    
                    if self.__game_rules.checkWin(self.__board, current_player.get_symbol()):
                        self.__board.display_board()
                        current_player.increment_score()
                        self.notify(f"{current_player.get_name()} wins!")
                        self.__game_over = True
                        return
                    
                    elif self.__game_rules.checkDraw(self.__board):
                        self.__board.display_board()
                        self.notify("It's a draw!")
                        self.__game_over = True
                        return
                    
                    # Rotate players
                    else:
                        self.__players.rotate(-1)
                else:
                    print("Invalid move! That spot is either out of bounds or already taken. Try again.")
                   
            except ValueError as e:
                print(e)
                continue
            