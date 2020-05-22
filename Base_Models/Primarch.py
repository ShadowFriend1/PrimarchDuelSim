from Base_Models.Infantry import Infantry, JumpInfantry


class FootPrimarch(Infantry):
    it_will_not_die = True
    eternal_warrior = True
    independent_character = True
    fearless = True
    fear = True
    adamantium_will = True
    fleet = True
    master_of_the_legion = True
    precision_shots = True
    precision_strikes = True


class JumpPrimarch(FootPrimarch, JumpInfantry):
    very_bulky = True
