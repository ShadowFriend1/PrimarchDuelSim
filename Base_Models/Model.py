class Model:
    ballistic_skill: int = 0
    psychic_mastery = 0
    accessible_lore = []
    psychic_powers = []
    it_will_not_die = False
    character = False
    fear = False
    adamantium_will = False
    master_of_the_legion = False
    precision_shots = False
    re_roll_all_hit_shoot: bool = False
    re_roll_all_wound_shoot: bool = False
    re_roll_num_hit_shoot: int = 0
    re_roll_num_wound_shoot: int = 0
    bulky = False
    very_bulky = False
    extremely_bulky = False

    def check_death(self):
        pass

    def add_hp(self):
        pass
