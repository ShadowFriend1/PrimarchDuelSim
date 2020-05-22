import random

from primarchs_deprecated.Primarch import Primarch


class Alpharius(Primarch):

    name = "Alpharius"
    ws = 7
    bs = 7
    ap = 1
    fp_i = True
    type = 20
    gun_str = 7
    gun_ap = 2
    shots = 2
    instant_d = True

    def hit(self, hit_mod, e_ws, a):
        hit_c = 4
        if self.blind[0]:
            hit_c = 6
        elif self.ws < (e_ws / 2):
            hit_c = 5
        elif self.ws > e_ws:
            hit_c = 3
        hit_c -= hit_mod
        if hit_c > 6:
            hit_c = 6
        elif hit_c < 2:
            hit_c = 2
        hits = 0
        for N in range(a):
            roll = random.randint(1, 6)
            if roll >= hit_c:
                hits += 1
            elif roll == 1:
                roll = random.randint(1, 6)
                if roll >= hit_c:
                    hits += 1
        return hits

    def wound(self, hits, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
        wound_c = 4
        if fp_t & fp_w:
            wound_c = 6
        elif fp_w:
            wound_c = 2
        elif strength == e_t + 1:
            wound_c = 3
        elif strength >= e_t + 2:
            wound_c = 2
        elif strength == e_t - 1:
            wound_c = 5
        elif strength <= e_t - 2:
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
                    wounds.append([ap, self.instant_d or (strength >= (e_t * 2)), roll])
                elif roll == 1:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, self.instant_d or (strength >= (e_t * 2)), roll])
        return wounds

    def shoot_hit(self, bs, shoot_hit_mod, shots):
        hits = 0
        gets_hot = []
        rerolls = 0
        if bs <= 5:
            hit_c = 7 - bs
            hit_c -= shoot_hit_mod
            if hit_c < 2:
                hit_c = 2
            elif hit_c > 6:
                hit_c = 6
            for N in range(shots):
                roll = random.randint(1, 6)
                if roll >= hit_c:
                    hits += 1
                elif roll == 1:
                    rerolls += 1
                    roll = random.randint(1, 6)
                    if roll >= hit_c:
                        hits += 1
                    elif roll == 1:
                        gets_hot.append([7, False, roll])
        else:
            hit_c_1 = 2
            hit_c_1 -= shoot_hit_mod
            if hit_c_1 < 2:
                hit_c_1 = 2
            elif hit_c_1 > 6:
                hit_c_1 = 6
            hit_c_2 = 7 - (bs - 5)
            hit_c_2 -= shoot_hit_mod
            if hit_c_2 < 2:
                hit_c_2 = 2
            elif hit_c_2 > 6:
                hit_c_2 = 6
            for N in range(shots):
                roll = random.randint(1, 6)
                if roll >= hit_c_1:
                    hits += 1
                elif roll == 1:
                    rerolls += 1
                    roll = random.randint(1, 6)
                    if roll >= hit_c_1:
                        hits += 1
                    elif roll == 1:
                        gets_hot.append([7, False, roll])
                else:
                    rerolls += 1
                    roll = random.randint(1, 6)
                    if roll >= hit_c_2:
                        hits += 1
                    elif roll == 1:
                        gets_hot.append([7, False, roll])
        if (hits + rerolls) < shots:
            if bs <= 5:
                hit_c = 7 - bs
                hit_c -= shoot_hit_mod
            else:
                hit_c = 2
                hit_c -= shoot_hit_mod
            if hit_c < 2:
                hit_c = 2
            elif hit_c > 6:
                hit_c = 6
            roll = random.randint(1, 6)
            if roll >= hit_c:
                hits += 1
            elif roll == 1:
                gets_hot.append([7, False, roll])
        self.save(gets_hot, False, False, False, False, True, False, False, False)
        return hits

    def shoot_wound(self, hits: int, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
        wound_c = 4
        if fp_t & fp_w:
            wound_c = 6
        elif fp_w:
            wound_c = 2
        elif strength - wound_mod == e_t + 1:
            wound_c = 3
        elif strength - wound_mod >= e_t + 2:
            wound_c = 2
        elif strength - wound_mod == e_t - 1:
            wound_c = 5
        elif strength - wound_mod <= e_t - 2:
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
                    wounds.append([ap, (strength >= (e_t * 2)), roll])
                elif roll == 1:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, (strength >= (e_t * 2)), roll])
        return wounds
