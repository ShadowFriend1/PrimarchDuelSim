import random

from Primarch import Primarch


class Fulgrim(Primarch):
    name = "Fulgrim"
    ws = 8
    bs = 6
    i = 8
    inv = 3
    type = 3
    gun_str = 5
    gun_ap = 5
    deflagrate = True
    shots = 2

    def fight(self, hit_mod, wound_mod, e_ws, e_t, fp_t, fp_i, e_i, dorn):
        bonus_a = self.i - e_i
        if bonus_a < 0:
            bonus_a = 0
        hits = super().hit(hit_mod, e_ws, self.a + bonus_a)
        return super().wound(hits, self.s, wound_mod, e_t, fp_t, fp_i, dorn, self.ap, self.fp_w), \
               self.concussive, self.blinding & hits > 0, self.disable, self.force, self.sever, \
               self.instant_d or (self.s > (2 * e_t))

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

class FulgrimLaer(Fulgrim):
    name = "Fulgrim With The Blade of The Laer"
    ap = 2


# TODO: implement murderous strike
class FulgrimFireblade(Fulgrim):
    name = "Fulgrim With FireBlade"
    ap = 2
    i = 9
    murderous = 0

    def hit_s(self, hit_mod, e_ws, a):
        hit_c = 4
        if self.blind:
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
            if roll >= 5:
                hits += 1
                self.murderous += 1
            elif roll >= hit_c:
                hits += 1
        return hits

    def hit(self, hit_mod, e_ws, a):
        hits = self.hit_s(hit_mod, e_ws, a)
        if hits < self.a:
            hits += self.hit_s(hit_mod, e_ws, 1)
        return hits

    def wound(self, hits: int, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
        wounds = super(FulgrimFireblade, self).wound(hits, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w)
        self.murderous = 0
        return wounds
