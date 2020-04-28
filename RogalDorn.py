import random

from Primarch import Primarch


class RogalDorn(Primarch):

    name = "Rogal Dorn"
    ws = 8
    a = 4
    type = 7
    dorn = True
    ap = 2
    shots = 5
    gun_ap = 4
    gun_str = 5

    def shoot_wound(self, hits: int, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
        wound_c = 4
        if fp_t & self.fp_w:
            wound_c = 6
        elif self.fp_w:
            wound_c = 2
        elif self.gun_str - wound_mod == e_t + 1:
            wound_c = 3
        elif self.gun_str - wound_mod >= e_t + 2:
            wound_c = 2
        elif self.gun_str - wound_mod == e_t - 1:
            wound_c = 5
        elif self.gun_str - wound_mod <= e_t - 2:
            wound_c = 6
        if dorn & (wound_c < 3):
            wound_c = 3
        wounds = []
        if not (fp_i & fp_w):
            for N in range(hits):
                roll = random.randint(1, 6)
                if roll == 6:
                    wounds.append(2)
                elif roll >= wound_c:
                    wounds.append(ap)
        return wounds

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
        wounds = []
        if not (fp_i & fp_w):
            for N in range(hits):
                roll = random.randint(1, 6)
                if roll >= wound_c:
                    wounds.append(ap)
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append(ap)
        return wounds

