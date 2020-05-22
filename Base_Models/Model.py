class Model:
    ballistic_skill: int = 0
    psychic_mastery = 0
    accessible_lore = []
    psychic_powers = []
    it_will_not_die = False
    re_roll_all_hit_shoot: bool = False
    re_roll_all_wound_shoot: bool = False
    re_roll_all_hit_combat: bool = False
    re_roll_all_wound_combat: bool = False
    re_roll_num_hit_shoot: int = 0
    re_roll_num_wound_shoot: int = 0
    re_roll_num_hit_combat: int = 0
    re_roll_num_wound_combat: int = 0

    def check_death(self):
        pass

    def add_hp(self):
        pass
