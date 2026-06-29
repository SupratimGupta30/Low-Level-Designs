from symbol import Symbol


class Board:
    def __init__(self, size: int):
        self.__size = size
        self.__empty_cell = Symbol('_')
        self.__board = [[self.__empty_cell for _ in range(self.__size)] for _ in range(self.__size)]

    def get_size(self):
        return self.__size

    def get_board(self):
        return self.__board

    def _get_cell_value(self, cell):
        if isinstance(cell, Symbol):
            return cell.get_symbol()
        return cell

    def is_cell_empty(self, row: int, col: int) -> bool:
        if not (0 <= row < self.__size and 0 <= col < self.__size):
            return False

        return self._get_cell_value(self.__board[row][col]) == self.__empty_cell.get_symbol()

    def set_cell(self, row: int, col: int, symbol: Symbol):
        if 0 <= row < self.__size and 0 <= col < self.__size:
            if self.is_cell_empty(row, col):
                self.__board[row][col] = symbol
                return True
            else:
                raise ValueError("Cell is already occupied.")
        else:
            raise IndexError("Row or column index out of bounds.")

    def get_cell(self, row: int, col: int):
        if 0 <= row < self.__size and 0 <= col < self.__size:
            return self.__board[row][col]
        else:
            raise IndexError("Row or column index out of bounds.")

    def is_full(self):
        for row in self.__board:
            if any(self._get_cell_value(cell) == self.__empty_cell.get_symbol() for cell in row):
                return False
        return True

    def display_board(self):
        for row in self.__board:
            print(" | ".join([self._get_cell_value(cell) for cell in row]))