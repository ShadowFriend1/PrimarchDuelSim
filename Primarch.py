import random


class Primarch:
    name = "generic"
    ws = 6
    ws_start = 0
    bs = 5
    s = 6
    s_start = 0
    t = 6
    w = 6
    w_c = 0
    i = 6
    a = 5
    ld = 10
    sv = 2
    inv = 4
    fp_t = False
    fp_i = False
    fp_w = False
    ap = 7
    hit_mod = 0
    shoot_hit_mod = 0
    shoot_wound_mod = 0
    wound_mod = 0
    shots = 0
    gun_str = 0
    gun_ap = 7
    fp_w_gun = False
    gun_concussive = False
    gun_blinding = False
    soul_blaze = False
    soul_blazed = 0
    deflagrate = False
    concussive = False
    concussed = []
    blinding = False
    blind = []
    disable = False
    sever = False
    force = False
    type = 0
    dorn = False
    asf = False
    turn = 1
    servo = False
    run = False
    instant_d = False
    fnp = 7
    reroll_sv = False

    def __init__(self):
        self.w_c = self.w
        self.ws_start = self.ws
        self.s_start = self.s
        self.concussed = [False, False]
        self.blind = [False, False]

    def get_fleshbane_tough(self):
        return self.fp_t

    def get_fleshbane_immune(self):
        return self.fp_i

    def get_initiative(self):
        if self.concussed[0]:
            return 1
        else:
            return self.i

    def get_toughness(self):
        return self.t

    def get_weapon_skill(self):
        if self.blind:
            return 1
        else:
            return self.ws

    def get_ballistic_skill(self):
        if self.blind:
            return 1
        else:
            return self.bs

    def get_hit_mod(self):
        return self.hit_mod

    def get_wound_mod(self):
        return self.wound_mod

    def get_wounds(self):
        return self.w_c

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_dorn(self):
        return self.dorn

    def get_asf(self):
        return self.asf

    def get_servo(self):
        return self.servo

    def get_sever(self):
        return self.sever

    def get_deflagrate(self):
        return self.deflagrate

    def get_soul_blaze(self):
        return self.soul_blaze

    def get_shoot_hit_mod(self):
        return self.shoot_hit_mod

    def get_shoot_wound_mod(self):
        return self.shoot_wound_mod

    def get_run(self):
        return self.run

    def reset(self, turn):
        self.w_c = self.w
        self.concussed[0] = False
        self.blind[0] = False
        self.ws = self.ws_start
        self.s = self.s_start
        self.turn = turn
        self.run = False

    def shoot(self, shoot_hit_mod, shoot_wound_mod, e_t, fp_t, fp_i, dorn, overwatch):
        if overwatch:
            hits = self.shoot_hit(1, shoot_hit_mod, self.shots)
        else:
            hits = self.shoot_hit(self.get_ballistic_skill(), shoot_hit_mod, self.shots)
        return self.shoot_wound(hits, self.gun_str, shoot_wound_mod, e_t, fp_t, fp_i, dorn, self.gun_ap, self.fp_w_gun), \
               self.gun_concussive, self.gun_blinding & hits > 0, self.deflagrate, self.soul_blaze, \
               (self.gun_str >= (e_t * 2))

    def shoot_hit(self, bs, shoot_hit_mod, shots):
        hits = 0
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
                else:
                    roll = random.randint(1, 6)
                    if roll >= hit_c_2:
                        hits += 1
        return hits

    def shoot_wound(self, hits: int, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
        wound_c = 4
        if fp_t & self.fp_w:
            wound_c = 6
        elif self.fp_w:
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
        return wounds

    def impact(self, wound_mod, e_t, dorn):
        return []

    def fight(self, hit_mod, wound_mod, e_ws, e_t, fp_t, fp_i, e_i, dorn):
        hits = self.hit(hit_mod, e_ws, self.a)
        return self.wound(hits, self.s, wound_mod, e_t, fp_t, fp_i, dorn, self.ap, self.fp_w), \
               self.concussive, self.blinding & hits > 0, self.disable, self.force, self.sever, \
               self.instant_d or (self.s > (2 * e_t))

    def servo_fight(self, hit_mod, wound_mod, e_ws, e_t, fp_t, dorn):
        hits = self.hit(hit_mod, e_ws, 1)
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
        if hits > 0:
            roll = random.randint(1, 6)
            if roll > wound_c:
                wounds.append(2)
        return wounds, False, False, False, False

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
        return hits

    def wound(self, hits: int, strength, wound_mod, e_t, fp_t, fp_i, dorn, ap, fp_w):
        wound_c = 4
        if fp_t & self.fp_w:
            wound_c = 6
        elif self.fp_w:
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
                    wounds.append(ap)
        return wounds

    def save(self, wounds, concussive, blinding, disable, force, shooting, sever, deflagrate, soul_blaze, instant_d):
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
                        if self.reroll_sv:
                            roll = random.randint(1, 6)
                            if roll < self.inv:
                                take.append(N)
                        else:
                            take.append(N)
                else:
                    if roll < self.sv:
                        take.append(N)
        for N in reversed(take):
            roll = random.randint(1, 6)
            if (roll >= self.fnp) & (not instant_d):
                take.remove(N)
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

    def wound_trigger(self):
        x = 0

    def check_death(self):
        if self.w_c > 0:
            self.wound_trigger()
            return False
        else:
            return True

    def end_of_turn(self):
        if self.turn // 2 == 0 & self.w_c < self.w:
            roll = random.randint(1, 6)
            if roll >= 5:
                self.w_c += 1
        if not self.concussed[1]:
            self.concussed[0] = False
        else:
            self.concussed[1] = False
        if not self.blind[1]:
            self.blind[0] = False
        else:
            self.blind[1] = False
        remove = 0
        for N in range(self.soul_blazed):
            roll = random.randint(1, 6)
            if roll >= 4:
                roll = random.randint(1, 3)
                self.save(self.wound(roll, 4, self.wound_mod, self.t, False, False, self.dorn, 5, False), False, False,
                          False, False, True, False, False, False, (4 >= (self.get_toughness()*2)))
            else:
                remove += 1
        self.soul_blazed -= remove
        self.turn += 1
