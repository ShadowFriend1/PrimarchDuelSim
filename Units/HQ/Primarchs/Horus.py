import random

from Primarch import Primarch


class Horus(Primarch):

    name = "Horus"
    ws = 8
    s = 7
    inv = 3
    type = 16
    gun_str = 5
    gun_ap = 3
    shots = 3

    def hit(self, hit_mod, e_ws, a):
        total_a = a
        if e_ws <= 4:
            total_a += random.randint(1, 3)
        return super().hit(hit_mod, e_ws, total_a)

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

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        roll = random.randint(1, 6)
        if roll > self.get_initiative() or roll == 6:
            roll = random.randint(1, 6)
            if roll < 3:
                self.blind[0] = blinding
                self.blind[1] = blinding
        take = []
        for N in wounds:
            if N[0] == 0:
                take.append(N)
            else:
                roll = random.randint(1, 6)
                if N[0] <= self.sv:
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
                            take.append([2, False, roll])
                    else:
                        if roll < self.sv:
                            take.append([2, False, roll])
        if len(take) > 0 & deflagrate:
            for N in take:
                roll = random.randint(1, 6)
                if N[0] <= self.sv:
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
            roll = random.randint(1, 6)
            if roll < 3:
                self.concussed[0] = concussive
                self.concussed[1] = concussive
            if disable:
                roll = random.randint(1, 6)
                if roll < 3:
                    self.ws -= 1
                    self.s -= 1
        return dead


class HorusWorldBreaker(Horus):

    name = "Horus With WorldBreaker"
    s = 10
    ap = 2
    concussive = True
    i = 1


class HorusTalon(Horus):

    name = "Horus With Talon"
    ap = 2
    disable = True

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


