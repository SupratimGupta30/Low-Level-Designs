from abc import ABC, abstractmethod
from symbol import Symbol
from board import Board

class GameRules(ABC):
    @abstractmethod
    def isvalidMove(self, board: Board, row: int, col: int):
        pass

    @abstractmethod
    def checkWin(self, board: Board, symbol: Symbol):
        pass

    @abstractmethod
    def checkDraw(self, board: Board):
        pass


class StandardGameRules(GameRules):
    def isvalidMove(self, board: Board, row: int, col: int):
        return board.is_cell_empty(row, col)

    def checkWin(self, board: Board, symbol: Symbol):
        size = board.get_size()
        # Check rows
        for row in range(size):
            if all(board.get_cell(row, col) == symbol.get_symbol() for col in range(size)):
                return True

        # Check columns
        for col in range(size):
            if all(board.get_cell(row, col) == symbol.get_symbol() for row in range(size)):
                return True

        # Check diagonals
        if all(board.get_cell(i, i) == symbol.get_symbol() for i in range(size)):
            return True
        if all(board.get_cell(i, size - 1 - i) == symbol.get_symbol() for i in range(size)):
            return True

        return False

    def checkDraw(self, board: Board):
        return board.is_full() and not self.checkWin(board, Symbol('X')) and not self.checkWin(board, Symbol('O'))