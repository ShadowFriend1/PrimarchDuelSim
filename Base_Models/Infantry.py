from Base_Models.Fighter import Fighter


class Infantry(Fighter):
    toughness: int = 0
    max_wounds: int = 0
    wounds: int = 0
    leadership: int = 0
    save: int = 7
    invulnerable_save: int = 7
    feel_no_pain: int = 7
    eternal_warrior = False
    fearless = False
    independent_character = False

    def __init__(self):
        self.wounds = self.max_wounds

    def check_death(self) -> bool:
        if self.wounds < 1:
            return True
        else:
            return False

    def add_hp(self):
        if self.wounds < self.max_wounds:
            self.wounds += 1


class JumpInfantry(Infantry):
    bulky = True
