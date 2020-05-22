from Base_Models.Unit import Unit
from typing import List


class Fight:
    player_1: List[Unit] = []
    player_2: List[Unit] = []

    def __init__(self, player_1: List[Unit], player_2: List[Unit]):
        self.player_1 = player_1
        self.player_2 = player_2

    # TODO: implement fight method
    def fight(self):
        i = 10
        while i > 0:
            for n in self.player_1:
                pass
            for n in self.player_2:
                pass
            i -= 1
