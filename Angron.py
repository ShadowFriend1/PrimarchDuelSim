import random

from Primarch import Primarch


class Angron(Primarch):

    name = "Angron"
    ws = 9
    s = 8
    i = 7
    a = 6
    ap = 2
    sv = 3
    type = 12
    shots = 1
    gun_ap = 2
    gun_str = 7

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
                roll = random.randint(1, 6)
                if roll != 6:
                    take.append(N)
            else:
                roll = random.randint(1, 6)
                if N <= self.sv:
                    if roll < self.inv:
                        roll = random.randint(1, 6)
                        if roll != 6:
                            take.append(N)
                else:
                    if roll < self.sv:
                        roll = random.randint(1, 6)
                        if roll != 6:
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


class BentAngron(Angron):

    name = "Angron With Extra Attack"
    a = 7
