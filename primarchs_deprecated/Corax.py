import random

from primarchs_deprecated.Primarch import Primarch


class Corax(Primarch):

    name = "Corax"
    ws = 7
    bs = 6
    i = 7
    a = 6
    inv = 5
    blinding = True
    ap = 2
    type = 19
    run = False
    shots = 2
    gun_ap = 3
    gun_str = 6

    def impact(self, wound_mod, e_t, dorn):
        return self.wound(random.randint(1, 3), 5, wound_mod, e_t, False, False, dorn, 3, False)

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
                    wounds.append([ap, self.instant_d, roll])
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, self.instant_d, roll])
        return wounds


class CoraxDeath(Corax):

    name = "Corax with Death Strike Active"

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
        if wound_c > 5:
            wound_c = 5
        wounds = []
        if not (fp_i & fp_w):
            for N in range(hits):
                roll = random.randint(1, 6)
                if roll >= wound_c:
                    wounds.append([ap, self.instant_d, roll])
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, self.instant_d, roll])
        return wounds


class CoraxScourge(Corax):

    name = "Corax with Scourge Active"

    def hit(self, hit_mod, e_ws, a):
        return super().hit(hit_mod, e_ws, a + random.randint(1, 3))


class CoraxShadow(Corax):

    name = "Corax with Shadow Walk Active"
    hit_mod = -1
