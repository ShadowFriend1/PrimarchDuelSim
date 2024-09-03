import random

from Primarch import Primarch


class Sanguinius(Primarch):

    name = "Sanguinius"
    type = 9
    ws = 9
    i = 7
    a = 6
    turn_start = 0
    shots = 2
    gun_ap = 1
    gun_str = 8

    def shoot(self, shoot_hit_mod, shoot_wound_mod, e_t, fp_t, fp_i, dorn, overwatch):
        hits = 0
        extra = 0
        if not overwatch:
            hits = self.shoot_hit(self.get_ballistic_skill(), shoot_hit_mod, self.shots)
            self.shots = 0
            extra = 2
        return self.shoot_wound(hits, self.gun_str, shoot_wound_mod, e_t, fp_t, fp_i, dorn, self.gun_ap, self.fp_w_gun) \
               + self.shoot_wound(extra, 6, shoot_wound_mod, e_t, fp_t, fp_i, dorn, 2, False), self.gun_concussive, \
               self.gun_blinding & hits > 0, self.deflagrate, self.soul_blaze

    def get_initiative(self):
        i = self.i
        if self.turn == 1:
            i += 1
        if self.concussed:
            return 1
        else:
            return i

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze):
        roll = random.randint(1, 6)
        if roll > self.get_initiative() or roll == 6:
            self.blind[0] = blinding
            self.blind[1] = blinding
        take = []
        if self.run:
            for N in wounds:
                if N[0] == 0:
                    take.append(N)
                else:
                    roll = random.randint(1, 6)
                    if N[0] <= self.sv:
                        if roll < self.inv:
                            roll = random.randint(1, 6)
                            if roll < self.inv:
                                take.append(N)
                    else:
                        if roll < self.sv:
                            take.append(N)
        else:
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
                            wounds.append([2, False, roll])
                    else:
                        if roll < self.sv:
                            wounds.append([2, False, roll])
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

    def reset(self, turn):
        super().reset(turn)
        self.turn_start = turn

    def hit(self, hit_mod, e_ws, a):
        if self.run:
            a += 1
        if self.turn == self.turn_start:
            return super().hit(hit_mod, e_ws, a + 1)
        else:
            return super().hit(hit_mod, e_ws, a)

    def end_of_turn(self):
        if (self.turn // 2) & (not self.run):
            roll = random.randint(1, 6)
            if (roll <= self.get_initiative()) & (roll != 6):
                self.run = True
        else:
            self.run = False
        super().end_of_turn()

    def impact(self, wound_mod, e_t, dorn):
        wounds = self.wound(1, 10, wound_mod, e_t, False, False, dorn, 2, False)
        return wounds


class SanguiniusBlade(Sanguinius):

    name = "Sanguinius With The Blade Encarmine"
    s = 7
    ap = 2

    def wound(self, hits, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
        wound_c = 4
        if fp_t & self.fp_w:
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


class SanguiniusSpear(Sanguinius):

    name = "Sanguinius With The Spear of Telesto"
    ap = 2
    instant_d = True

    def fight(self, hit_mod, wound_mod, e_ws, e_t, fp_t, fp_i, e_i, dorn):
        s = self.s
        ap = self.ap
        if self.run:
            s += 3
            ap = 1
        hits = self.hit(hit_mod, e_ws, self.a)
        return self.wound(hits, s, wound_mod, e_t, fp_t, fp_i, dorn, ap, self.fp_w), \
               self.concussive, self.blinding & hits > 0, self.disable, self.force, self.sever, \
               self.instant_d or (self.s >= (e_t*2))

    def hit(self, hit_mod, e_ws, a):
        hits = super().hit(hit_mod, e_ws, a)
        if hits < self.a:
            hits += super().hit(hit_mod, e_ws, 1)
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
                    if roll == 6:
                        wounds.append([ap, self.instant_d or (strength >= (e_t * 2)), roll])
        return wounds


class SanguiniusMoonsilver(Sanguinius):

    name = "Sanguinius With The Moonsilver Blade"
    ap = 3
    blinding = True
    i = 8

    def hit(self, hit_mod, e_ws, a):
        hits = super().hit(hit_mod, e_ws, a)
        if hits < self.a:
            hits += super().hit(hit_mod, e_ws, 1)
        return hits