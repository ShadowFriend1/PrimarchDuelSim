from typing import List
from Base_Models.Unit import Unit
from Turns.Roll import Roll


class PlayerTurn:
    player_1: List[Unit] = []
    player_2: List[Unit] = []

    def __init__(self, player_1: List[Unit], player_2: List[Unit]):
        self.player_1 = player_1
        self.player_2 = player_2

    def start(self):
        self.move()
        self.psychic()
        self.shoot()
        self.fight()

    def move(self):
        for n in self.player_1:
            pass

    def psychic(self):
        for n in self.player_1:
            pass

    def shoot(self):
        for n in self.player_1:
            pass

    def charge(self):
        for n in self.player_1:
            pass

    def fight(self):
        i = 10
        while i > 0:
            for n in self.player_1:
                pass
            for n in self.player_2:
                pass
            i -= 1

    def end_of_turn(self):
        for x in self.player_1:
            for n in x.get_models():
                if n.__getattribute__("it_will_not_die"):
                    roll = Roll(1)
                    if roll.get_roll()[0] >= 5:
                        n.add_hp()
