import random

from Primarch import Primarch


class Mortarion(Primarch):

    name = "Mortarion"
    ws = 7
    s = 7
    t = 7
    w = 7
    i = 4
    ap = 2
    fp_t = True
    type = 14
    gun_ap = 2
    gun_str = 8
    shots = 1

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
                          False, False, True, False, False, False)
            else:
                remove += 1
        self.soul_blazed -= remove
        self.turn += 1
