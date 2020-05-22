from Base_Models.Fighter import Fighter
from Base_Models.Model import Model


class Vehicle(Model):
    front_armour: int = 0
    side_armour: int = 0
    rear_armour: int = 0
    max_hull_points: int = 0
    hull_points: int = 0

    def __init__(self):
        self.hull_points = self.max_hull_points

    def check_death(self) -> bool:
        if self.hull_points < 1:
            return True
        else:
            return False

    def add_hp(self):
        if self.hull_points < self.max_hull_points:
            self.hull_points += 1


class Walker(Vehicle, Fighter):
    pass
