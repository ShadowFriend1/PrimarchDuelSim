import random

from Primarch import Primarch


class Lorgar(Primarch):

    name = "Lorgar"
    s = 8
    bs = 6
    a = 4
    ap = 2
    concussive = True
    type = 17
    shots = 1
    gun_ap = 3
    gun_str = 6

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

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        if force:
            self.inv -= 1
        dead = super().save(wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze)
        if force:
            self.inv += 1
        return dead

    def hit(self, hit_mod, e_ws, a):
        hits = super().hit(hit_mod, e_ws, a)
        if hits < self.a:
            hits += super().hit(hit_mod, e_ws, 1)
        return hits


class LorgarEmpowered(Lorgar):

    name = "Lorgar With Psychic Buff"
    reroll_sv = True

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
                    wounds.append([ap, (strength >= (e_t * 2)), roll])
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, (strength >= (e_t * 2)), roll])
        return wounds

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
                    wounds.append([ap, self.instant_d or (strength >= (e_t * 2)), roll])
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, self.instant_d or (strength >= (e_t * 2)), roll])
        return wounds

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        if force:
            self.inv -= 1
        dead = super().save(wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze)
        if force:
            self.inv += 1
        return dead

import random

from Primarch import Primarch


class KonradCurze(Primarch):

    name = "Konrad Curze"
    ws = 8
    bs = 6
    i = 7
    ap = 2
    type = 8
    a = 6
    shots = 3
    gun_str = 4
    gun_ap = 5
    murderous = 6

    def impact(self, wound_mod, e_t, dorn):
        wounds = self.wound(random.randint(1, 3), self.s, wound_mod, e_t, False, False, dorn, 7, False)
        return wounds

    def hit(self, hit_mod, e_ws, a):
        if self.run:
            return super().hit(hit_mod, e_ws, a + 1)
        else:
            return super().hit(hit_mod, e_ws, a)

    def end_of_turn(self):
        if self.turn // 2:
            roll = random.radint(1, 6)
            if (roll <= self.get_initiative()) & (roll != 6):
                self.run = True
        else:
            self.run = False
        super().end_of_turn()

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
                if roll == 6:
                    wounds.append([0, self.instant_d, roll])
                elif roll >= wound_c:
                    wounds.append([ap, self.instant_d, roll])
        return wounds




    def wound(self, hits
    , strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
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
                if roll >= self.murdrous:
                    wounds.append([ap, True, roll])
                elif roll >= wound_c:
                    wounds.append([ap, self.instant_d, roll])
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, self.instant_d, roll])
        return wounds


import random

from Primarch import Primarch


class LemanRuss(Primarch):

    ws = 9
    bs = 6
    i = 7
    a = 6
    hit_mod = -1
    name = "Leman Russ"
    type = 6
    shots = 3
    gun_str = 4
    gun_ap = 3

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
                if roll == 6:
                    wounds.append([2, self.instant_d, roll])
                elif roll >= wound_c:
                    wounds.append([ap, self.instant_d, roll])
        return wounds


class LemanRussBalenight(LemanRuss):

    name = "Leman Russ With The Sword of Balenight"
    ap = 2
    sever = True

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
        elif self.s== e_t - 1:
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
                    wounds.append([ap, self.instant_d, roll])
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, self.instant_d, roll])
        return wounds


class LemanRussHelwinter(LemnRuss):

    name = "Leman Russ With The Axe of Helwinter"
    s = 8
    ap = 2

    def hit(self, hit_mod, e_ws, a):
        hits = super().hit(hit_mod, e_ws, a)
        if hits < self.a:
            hits += supe().hit(hit_mod, e_ws, 1)
        return hits
