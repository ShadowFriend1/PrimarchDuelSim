import random

from Primarch import Primarch


class Lion(Primarch):

    name = "Lion El Johnson"
    ws = 8
    s = 7
    i = 7
    type = 1

    def hit(self, hit_mod, e_ws, a):
        hit_c = 4
        if (self.ws > e_ws) & (not self.blind):
            hit_c = 3
        hit_c -= hit_mod
        if hit_c > 4:
            hit_c = 4
        elif hit_c < 2:
            hit_c = 2
        hits = 0
        for N in range(a):
            roll = random.randint(1, 6)
            if roll >= hit_c:
                hits += 1
        return hits

    def wound_trigger(self):
        if self.w <= 2:
            self.a = 7
        elif self.w <= 4:
            self.a = 6


class LionSword(Lion):

    name = "Lion El Johnson With The Lion Sword"
    ap = 1
    fp_w = True

    def hit(self, hit_mod, e_ws, a):
        hits = super().hit(hit_mod, e_ws, a)
        if hits < self.a:
            hits += super().hit(hit_mod, e_ws, 1)
        return hits


class LionWolf(Lion):

    name = "Lion El Johnson With The Wolf Blade"
    s = 10
    ap = 2

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
        if not (fp_i & self.fp_w):
            for N in range(hits):
                roll = random.randint(1, 6)
                if roll >= wound_c:
                    wounds.append(self.ap)
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append(self.ap)
        return wounds

