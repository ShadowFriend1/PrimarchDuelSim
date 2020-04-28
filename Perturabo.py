import random

from Primarch import Primarch


class Perturabo(Primarch):

    name = "Perturabo"
    ws = 8
    bs = 6
    s = 7
    a = 4
    inv = 3
    ap = 2
    type = 4
    gun_ap = 3
    gun_str = 6
    shots = 3

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

    def shoot_hit(self, bs, shoot_hit_mod, shots):
        hits = 0
        if bs <= 5:
            hit_c = 7 - bs
        else:
            hit_c = 2
        hit_c -= shoot_hit_mod
        if hit_c < 2:
            hit_c = 2
        elif hit_c > 6:
            hit_c = 6
        for N in range(shots):
            roll = random.randint(1, 6)
            if roll >= hit_c:
                hits += 1
            else:
                roll = random.randint(1, 6)
                if roll >= hit_c:
                    hits += 1
        return hits


class PerturaboHammer(Perturabo):

    name = "Perturabo With ForgeBreaker"
    s = 10
    sp = 1
    i = 1
    concussive = True
    blinding = True
