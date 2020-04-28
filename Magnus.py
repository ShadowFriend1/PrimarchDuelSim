import random

from Primarch import Primarch


class Magnus(Primarch):

    name = "Magnus With No Powers"
    ws = 7
    s = 9
    a = 4
    ap = 1
    force = True
    hit_mod = -1
    type = 15
    shoot_hit_mod = -1
    gun_ap = 2
    gun_str = 8
    shots = random.randint(1, 3)
    soul_blaze = True

    def shoot(self, shoot_hit_mod, shoot_wound_mod, e_t, fp_t, fp_i, dorn, overwatch):
        if overwatch:
            hits = self.shoot_hit(1, shoot_hit_mod, self.shots)
        else:
            hits = self.shoot_hit(self.get_ballistic_skill(), shoot_hit_mod, self.shots)
        self.shots = random.randint(1, 3)
        return self.shoot_wound(hits, self.gun_str, shoot_wound_mod, e_t, fp_t, fp_i, dorn, self.gun_ap, self.fp_w_gun),\
               self.gun_concussive, self.gun_blinding & hits > 0, self.deflagrate, self.soul_blaze


class MagnusIronArm(Magnus):

    name = "Magnus With Iron Arm"
    s = 10
    t = 9


class MagnusEndurance(Magnus):

    name = "Magnus With Endurance"

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        roll = random.randint(1, 6)
        if roll > self.get_initiative() or roll == 6:
            self.blind[0] = blinding
            self.blind[1] = blinding
        take = []
        for N in wounds:
            if N == 0:
                roll = random.randint(1, 6)
                if roll < 4:
                    take.append(N)
            else:
                roll = random.randint(1, 6)
                if N <= self.sv:
                    if roll < self.inv:
                        roll = random.randint(1, 6)
                        if roll < 4:
                            take.append(N)
                else:
                    if roll < self.sv:
                        roll = random.randint(1, 6)
                        if roll < 4:
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


class MagnusWarpSpeed(Magnus):

    name = "Magnus With Warp Speed"
    a = 7
    i = 9


class MagnusAllBiomancy(Magnus):

    name = "Magnus With All Biomancy Powers"
    s = 10
    t = 9
    i = 9
    a = 7

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        roll = random.randint(1, 6)
        if roll > self.get_initiative() or roll == 6:
            self.blind[0] = blinding
            self.blind[1] = blinding
        take = []
        for N in wounds:
            if N == 0:
                roll = random.randint(1, 6)
                if roll < 4:
                    take.append(N)
            else:
                roll = random.randint(1, 6)
                if N <= self.sv:
                    if roll < self.inv:
                        roll = random.randint(1, 6)
                        if roll < 4:
                            take.append(N)
                else:
                    if roll < self.sv:
                        roll = random.randint(1, 6)
                        if roll < 4:
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


class MagnusPrecognition(Magnus):

    name = "Magnus With Precognition"

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
                if N <= self.sv:
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