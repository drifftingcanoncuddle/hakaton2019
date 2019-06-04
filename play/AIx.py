import random
import pickle

from play.Plane import Plane



class AIx:
    def __init__(self):
        # hash, prob
        self.moves = dict()
        self.made_moves = list()

        self.read_moves_table()

    def read_moves_table(self):
        with open("moves_x.mv", "rb") as file:
            self.moves = pickle.load(file)

    def save_moves_table(self):
        with open("moves_x.mv", "wb") as file :
            pickle.dump(self.moves, file)

    def play(self, plane) -> (int, int):
        choice = self.chose_move(plane)
        self.made_moves.append(
            (choice, plane.get_hash())
        )
        return choice

    def chose_move(self, plane: Plane):
        plane_hash = plane.get_hash()
        if plane_hash in self.moves.keys():
            # chose from already played moves
            prob = self.moves[plane_hash]
            choice = random.randint(0, 900)
            actual = 0
            field = 0
            while choice > actual:
                actual += prob[field]
                field += 1

            return field // 3 + field % 3

        else:
            # create new entry
            self.moves[plane_hash] = [100,100,100,100,100,100,100,100,100]
            return random.randint(0,2), random.randint(0, 2)

    def loose(self):
        for choice, hash in self.made_moves:
            field = choice[0] * 3 + choice[1]
            for f in range(9):
                if f == field:
                    self.moves[hash][f] -= 8
                else;
                self.moves[hash][f] += 1
        self.save_moves_table()

    def win(self):
        for choice, hash in self.made_moves:
            field = choice[0] * 3 + choice[1]
            for f in range(9):
                if f == field:
                    self.moves[hash][f] += 8
                else;
                self.moves[hash][f] -= 1
        self.save_moves_table()
