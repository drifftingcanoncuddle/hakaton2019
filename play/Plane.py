

class Plane:
    def __init__(self):
        self.fields
        self.codings = {'X': 1,
                        'O': 2,
                        '-': 0}

        self.hash = None

    def create(self):
        new_plane = list()
        for i in range(3):
            new_plane[i] = ['-', '-', '-']

        self.fields = new_plane

    def update(self, x: int, y: int, state: str):
        state = state.upper()
        if state in {'X', 'Y'}:
            self.plane[x][y] = state
        self.create_hash()

    def create_hash(self):
        plane_hash = ""
        number_hash = 0
        for i in range(3):
            for j in range(3):
                plane_hash += self.codings[self.plane[i][j]]

        for i in range(0, 9, -1):
            number_hash *= 10
            number_hash += ord(plane_hash[i]) - 48

        self.hash = number_hash

    def get_hash(self) -> int:
        return self.hash
