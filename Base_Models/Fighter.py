from Base_Models.Model import Model


class Fighter(Model):
    weapon_skill: int = 0
    attacks: int = 0
    initiative: int = 0
    strength: int = 0
    fleet = False
    precision_strikes = False
    re_roll_num_hit_combat: int = 0
    re_roll_num_wound_combat: int = 0
    re_roll_all_hit_combat: bool = False
    re_roll_all_wound_combat: bool = False
