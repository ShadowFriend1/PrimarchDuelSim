from Base_Models.Fighter import Fighter


class Infantry(Fighter):
    toughness: int = 0
    wounds: int = 0
    leadership: int = 0
    save: int = 7
    invulnerable_save: int = 7
    feel_no_pain: int = 7
