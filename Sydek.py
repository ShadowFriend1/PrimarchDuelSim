import random

from Primarch import Primarch


class Sydek(Primarch):

    name = "Sydek Akadius"
    ws = 6
    bs = 9
    s = 5
    i = 7
    a = 4
    ap = 3
    type = 11
    run = False

    def hit(self, hit_mod, e_ws, a):
        if self.run:
            return super().hit(hit_mod, e_ws, a + 1)
        else:
            return super().hit(hit_mod, e_ws, a)

    def end_of_turn(self):
        if self.turn // 2:
            roll = random.randint(1, 6)
            if (roll <= self.get_initiative()) & (roll != 6):
                self.run = True
        else:
            self.run = False
        super().end_of_turn()

    def wound(self, hits, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
        wound_c = 4
        if fp_t & self.fp_w:
            wound_c = 6
        elif self.fp_w:
            wound_c = 2
        elif self.s == e_t + 1:
            wound_c = 3
        elif self.s >= e_t + 2:
            wound_c = 2
        elif self.s == e_t - 1:
            wound_c = 5
        elif self.s <= e_t - 2:
            wound_c = 6
        if wound_c < 6 & wound_mod < 0:
            wound_c -= wound_mod
        elif wound_c > 2 & wound_mod > 0:
            wound_c -= wound_mod
        if dorn & (wound_c < 3):
            wound_c = 3
        if wound_c > 5:
            wound_c = 5
        wounds = []
        if not (fp_i & fp_w):
            for N in range(hits):
                roll = random.randint(1, 6)
                if roll >= wound_c:
                    if roll == 6:
                        wounds.append(2)
                    elif roll >= wound_c:
                        wounds.append(ap)
                else:
                    roll = random.randint(1, 6)
                    if roll == 6:
                        wounds.append(2)
                    elif roll >= wound_c:
                        wounds.append(ap)
        return wounds


class SydekAbyss(Sydek):

    name = "Sydek Using Abyss"
    gun_ap = 2
    gun_str = 8
    shots = 5
    fp_w_gun = True

class SydekDriver(Sydek):

    name = "Sydek Using Driver and Chase"
    gun_ap = 3
    gun_str = 6
    shots = 3
    deflagrate = True
    gun_blinding = True

    def shoot(self, shoot_hit_mod, shoot_wound_mod, e_t, fp_t, fp_i, dorn, overwatch):
        hits = 0
        if not overwatch:
            hits = 2
        return self.shoot_wound(hits, self.gun_str, shoot_wound_mod, e_t, fp_t, fp_i, dorn, self.gun_ap, self.fp_w_gun), \
               self.gun_concussive, self.gun_blinding & hits > 0, self.deflagrate, self.soul_blaze

