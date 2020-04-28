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
        roll = random.randint(1, 6)
        if roll > self.get_initiative() or roll == 6:
            self.blind[0] = blinding
            self.blind[1] = blinding
        take = []
        for N in wounds:
            if N == 0:
                take.append(N)
            else:
                roll = random.randint(1, 6)
                if N <= self.sv & force:
                    if roll < (self.inv - 1):
                        take.append(N)
                elif N <= self.sv:
                    if roll < self.inv:
                        take.append(N)
                else:
                    if roll < self.sv:
                        take.append(N)
        if len(take) > 0 & sever:
            roll = random.randint(1, 6) + random.randint(1, 6)
            if roll > self.t:
                for N in range(random.randint(1, 3)):
                    roll = random.randint(1, 6)
                    if 2 <= self.sv:
                        if roll < self.inv:
                            take.append(2)
                    else:
                        if roll < self.sv:
                            take.append(2)
        if len(take) > 0 & deflagrate:
            for N in take:
                roll = random.randint(1, 6)
                if N <= self.sv:
                    if roll < self.inv:
                        take.append(N)
                else:
                    if roll < self.sv:
                        take.append(N)
        if len(take) > 0 & soul_blaze:
            self.soul_blazed += 1
        self.w_c -= len(take)
        dead = self.check_death()
        if len(take) > 0 & (not dead):
            self.concussed[0] = concussive
            self.concussed[1] = concussive
            if disable:
                self.ws -= 1
                self.s -= 1
        return dead

    def hit(self, hit_mod, e_ws, a):
        hits = super().hit(hit_mod, e_ws, a)
        if hits < self.a:
            hits += super().hit(hit_mod, e_ws, 1)
        return hits


class LorgarEmpowered(Lorgar):

    name = "Lorgar With Psychic Buff"

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
                if roll >= wound_c:
                    wounds.append(ap)
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append(ap)
        return wounds

    def hit(self, hit_mod, e_ws, a):
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
            if roll >= hit_c:
                hits += 1
            else:
                roll = random.randint(1, 6)
                if roll >= hit_c:
                    hits += 1
        return hits

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

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        roll = random.randint(1, 6)
        if roll > self.get_initiative() or roll == 6:
            self.blind[0] = blinding
            self.blind[1] = blinding
        take = []
        for N in wounds:
            if N == 0:
                take.append(N)
            else:
                roll = random.randint(1, 6)
                if N <= self.sv & force:
                    if roll < (self.inv - 1):
                        roll = random.randint(1, 6)
                        if roll < (self.inv - 1):
                            take.append(N)
                elif N <= self.sv:
                    if roll < self.inv:
                        roll = random.randint(1, 6)
                        if roll < self.inv:
                            take.append(N)
                else:
                    if roll < self.sv:
                        roll = random.randint(1, 6)
                        if roll < self.sv:
                            take.append(N)
        if len(take) > 0 & sever:
            roll = random.randint(1, 6) + random.randint(1, 6)
            if roll > self.t:
                for N in range(random.randint(1, 3)):
                    roll = random.randint(1, 6)
                    if 2 <= self.sv:
                        if roll < self.inv:
                            take.append(2)
                    else:
                        if roll < self.sv:
                            take.append(2)
        if len(take) > 0 & deflagrate:
            for N in take:
                roll = random.randint(1, 6)
                if N <= self.sv:
                    if roll < self.inv:
                        take.append(N)
                else:
                    if roll < self.sv:
                        take.append(N)
        if len(take) > 0 & soul_blaze:
            self.soul_blazed += 1
        self.w_c -= len(take)
        dead = self.check_death()
        if len(take) > 0 & (not dead):
            self.concussed[0] = concussive
            self.concussed[1] = concussive
            if disable:
                self.ws -= 1
                self.s -= 1
        return dead
