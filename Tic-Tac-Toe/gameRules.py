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

    def _get_cell_value(self, board: Board, row: int, col: int):
        cell = board.get_cell(row, col)
        return cell.get_symbol() if isinstance(cell, Symbol) else cell

    def checkWin(self, board: Board, symbol: Symbol):
        size = board.get_size()
        target = symbol.get_symbol()

        # Check rows
        for row in range(size):
            if all(self._get_cell_value(board, row, col) == target for col in range(size)):
                return True

        # Check columns
        for col in range(size):
            if all(self._get_cell_value(board, row, col) == target for row in range(size)):
                return True

        # Check diagonals
        if all(self._get_cell_value(board, i, i) == target for i in range(size)):
            return True
        if all(self._get_cell_value(board, i, size - 1 - i) == target for i in range(size)):
            return True

        return False

    def checkDraw(self, board: Board):
        return board.is_full() and not self.checkWin(board, Symbol('X')) and not self.checkWin(board, Symbol('O'))