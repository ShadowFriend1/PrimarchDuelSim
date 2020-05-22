import random

from primarchs_deprecated.Primarch import Primarch


class Khan(Primarch):
    name = "Khan"
    type = 5
    ws = 7
    bs = 6
    a = 6
    ap = 2
    inv = 3
    asf = True

    def end_of_turn(self):
        if self.turn // 2:
            roll = random.randint(1, 6)
            if (roll <= self.get_initiative()) & (roll != 6):
                self.run = True
        else:
            self.run = False
        super().end_of_turn()

    def hit(self, hit_mod, e_ws, a):
        if self.run:
            hits = super().hit(hit_mod, e_ws, a + 1)
        else:
            hits = super().hit(hit_mod, e_ws, a)
        if hits < self.a:
            hits += super().hit(hit_mod, e_ws, 1)
        return hits

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        roll = random.randint(1, 6)
        if roll > self.get_initiative() or roll == 6:
            self.blind[0] = blinding
            self.blind[1] = blinding
        take = []
        for N in wounds:
            roll = random.randint(1, 6)
            if N[0] <= self.sv & shooting:
                if roll < self.inv + 2:
                    take.append(N)
            elif N[0] <= self.sv:
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
            self.concussed[0] = concussive
            self.concussed[1] = concussive
            if disable:
                self.ws -= 1
                self.s -= 1
        return dead


class KhanAfoot(Khan):
    name = "The Khan Afoot"
    i = 9
    gun_str = 6
    gun_ap = 3
    shots = 1

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


class KhanMounted(Khan):
    name = "The Khan Mounted"
    i = 8
    t = 7
    gun_str = 5
    gun_ap = 4
    shots = 3

    def impact(self, wound_mod, e_t, dorn):
        return self.wound(random.randint(1, 3), self.s, wound_mod, e_t, False, False, dorn, 7, False)

    def shoot(self, shoot_hit_mod, shoot_wound_mod, e_t, fp_t, fp_i, dorn, overwatch):
        if overwatch:
            hits = self.shoot_hit(1, shoot_hit_mod, self.shots) + \
                   self.shoot_hit(1, shoot_hit_mod, self.shots)
        else:
            hits = self.shoot_hit(self.get_ballistic_skill(), shoot_hit_mod, self.shots) + \
                   self.shoot_hit(self.get_ballistic_skill(), shoot_hit_mod, self.shots)
        return self.shoot_wound(hits, self.gun_str, shoot_wound_mod, e_t, fp_t, fp_i, dorn, self.gun_ap, self.fp_w_gun), \
               self.gun_concussive, self.gun_blinding & hits > 0, self.deflagrate, self.soul_blaze, \

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
