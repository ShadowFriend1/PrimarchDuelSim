import random

from Primarch import Primarch


class Leandros(Primarch):

    name = "Leandros Vettias"
    ws = 8
    s = 8
    inv = 3
    type = 2
    shots = 1
    gun_ap = 3
    gun_str = 6

    def get_initiative(self):
        return self.i

    def check_death(self):
        death = super().check_death()
        self.s += 1
        return death

    def shoot_hit(self, bs, shoot_hit_mod, shots):
        hits = 0
        reroll = True
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
                elif reroll:
                    roll = random.randint(1, 6)
                    reroll = False
                    if roll >= hit_c:
                        hits += 1
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
                elif reroll:
                    roll = random.randint(1, 6)
                    reroll = False
                    if roll >= hit_c_1:
                        hits += 1
                else:
                    roll = random.randint(1, 6)
                    if roll >= hit_c_2:
                        hits += 1
        return hits


class LeandrosBlade(Leandros):

    name = "Leandros With The Blade of Lycetta"
    ap = 1


class LeandrosShield(Leandros):

    name = "Leandros With The Shield of Pontia"
    ap = 2
    concussive = True