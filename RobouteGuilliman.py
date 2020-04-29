import random

from Primarch import Primarch


class RobouteGuilliman(Primarch):

    name = "Roboute Guilliman"
    ws = 7
    start_ws = 7
    bs = 6
    a = 5
    type = 13
    shots = 2
    gun_ap = 3
    gun_str = 6

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
                    wounds.append([2, (strength >= (e_t * 2)), roll])
                elif roll >= wound_c:
                    wounds.append([ap, (strength >= (e_t * 2)), roll])
        return wounds

    def get_initiative(self):
        return self.i

    def check_death(self):
        death = super().check_death()
        if self.ws < 10:
            self.ws += 1
        return death

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        roll = random.randint(1, 6)
        if roll > self.get_initiative() or roll == 6:
            self.blind[0] = blinding
            self.blind[1] = blinding
        inv_roll = True
        take = []
        for N in wounds:
            if N == 0:
                take.append(N)
            else:
                roll = random.randint(1, 6)
                if N[0] <= self.sv:
                    if (roll < self.inv) & inv_roll:
                        roll = random.randint(1, 6)
                        if roll < self.inv:
                            take.append(N)
                            inv_roll = True
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


class RobouteGuillimanGladius(RobouteGuilliman):

    name = "Roboute Guilliman With Gladius"
    s = 7
    ap = 2
    murderous = 6

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
                if roll >= self.murderous:
                    wounds.append([ap, True, roll])
                elif roll >= wound_c:
                    wounds.append([ap, self.instant_d, roll])
                else:
                    roll = random.randint(1, 6)
                    if roll >= wound_c:
                        wounds.append([ap, self.instant_d, roll])
        return wounds


class RobouteGuillimanHand(RobouteGuilliman):

    name = "Roboute Guilliman With Hand"
    s = 10
    ap = 1
    i = 1
    concussive = True