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
        self.check_dead()

    def psychic(self):
        for n in self.player_1:
            pass
        self.check_dead()

    def shoot(self):
        for n in self.player_1:
            pass
        self.check_dead()

    def charge(self):
        for n in self.player_1:
            pass
        self.check_dead()

    def fight(self):
        i = 10
        while i > 0:
            for n in self.player_1:
                pass
            for n in self.player_2:
                pass
            self.check_dead()
            i -= 1

    def check_dead(self):
        for x in reversed(self.player_1):
            for n in reversed(x.get_models()):
                if n.check_death():
                    x.get_models().remove(n)
            if len(x.get_models()) == 0:
                self.player_1.remove(x)
        for x in reversed(self.player_2):
            for n in reversed(x.get_models()):
                if n.check_death():
                    x.get_models().remove(n)
            if len(x.get_models()) == 0:
                self.player_2.remove(x)

    def end_of_turn(self) -> int:
        for x in self.player_1:
            for n in x.get_models():
                if n.it_will_not_die:
                    roll = Roll(1)
                    if roll.get_roll()[0] >= 5:
                        n.add_hp()
        if len(self.player_1) + len(self.player_2) == 0:
            return 3
        elif len(self.player_1) == 0:
            return 1
        elif len(self.player_2) == 0:
            return 2
        else:
            return 0
