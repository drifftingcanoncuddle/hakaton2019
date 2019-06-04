from typing import *
from play.Plane import Plane
from play.AIx import AIx

class Controler:
    def __init__(self):
        self.plane = Plane()
        self.plane.create()
        self.user_symbol = "O"
        self.ai_symbol = "O"
        self.ai = AIx()

    def set_symbols(self, user_symbol: str, ai_symbol: str):
        self.ai_symbol = ai_symbol
        self.user_symbol = user_symbol

    def play(self, user_x: int, user_y: int):
        self.plane.update(user_x, user_y, self.user_symbol)
        ai_x, ai_y = self.ai.play(self.plane)
        self.plane.update(ai_x, ai_y, self.ai_symbol)

    def ai_win(self):
        pass

    def win(self, plane):
        # left diagonal
        if plane[0][0] == plane[1][1] and plane[1][1] == plane[2][2]:
            return plane[0][0]

        # right diagonal
        elif plane[2][0] == plane[1][1] and plane[0][2] == plane[1][1]:
            return plane[1][1]

        # l3 vertical
        elif plane[0][0] == plane[0][1] and plane[0][1] == plane[0][2]:
            return plane[0][1]

        # l2 vertical
        elif plane[1][0] == plane[1][1] and plane[1][1] == plane[1][2]:
            return plane[1][1]

        # l1 vertical
        elif plane[2][0] == plane[2][1] and plane[2][1] == plane[2][2]:
            return plane[2][1]

        # l3 horizontal
        elif plane[0][0] == plane[1][0] and plane[1][0] == plane[2][0]:
            return plane[0][1]

        # l2 horizontal
        elif plane[0][1] == plane[1][1] and plane[1][1] == plane[2][1]:
            return plane[0][1]

        # l1 horizontal
        elif plane[0][2] == plane[1][2] and plane[1][2] == plane[2][2]:
            return plane[0][1]
