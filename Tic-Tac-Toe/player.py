from symbol import Symbol

class Player:
    def __init__(self, id: int, name: str, symbol: Symbol):
        self.__id = id
        self.__name = name
        self.__symbol = symbol
        self.score = 0  # Initialize score to 0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol
    
    def get_score(self):
        return self.score
    
    def increment_score(self):
        self.score += 1