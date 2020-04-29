import random

from Primarch import Primarch


class Vulkan(Primarch):

    name = "Vulkan"
    ws = 7
    s = 10
    t = 7
    i = 5
    a = 4
    ap = 1
    inv = 3
    concussive = True
    type = 18
    instant_d = True

    def end_of_turn(self):
        if self.turn // 2 == 0 & self.w_c < self.w:
            roll = random.randint(1, 6)
            if roll >= 5:
                self.w_c += 1
            else:
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

    def shoot(self, shoot_hit_mod, shoot_wound_mod, e_t, fp_t, fp_i, dorn, overwatch):
        if overwatch:
            wounds = self.wound(random.randint(1, 3), 6, shoot_wound_mod, e_t, fp_t, fp_i, dorn, 4, False)
        else:
            wounds = self.wound(1, 6, shoot_wound_mod, e_t, fp_t, fp_i, dorn, 4, False)
        return wounds, False, False, False, False
