import random

from Primarch import Primarch


class KonradCurze(Primarch):

    name = "Konrad Curze"
    ws = 8
    bs = 6
    i = 7
    ap = 2
    type = 8
    a = 6
    shots = 3
    gun_str = 4
    gun_ap = 5

    def impact(self, wound_mod, e_t, dorn):
        wounds = self.wound(random.randint(1, 3), self.s, wound_mod, e_t, False, False, dorn, 7, False)
        return wounds

    def hit(self, hit_mod, e_ws, a):
        if self.run:
            return super().hit(hit_mod, e_ws, a + 1)
        else:
            return super().hit(hit_mod, e_ws, a)

    def end_of_turn(self):
        if self.turn // 2:
            roll = random.randint(1, 6)
            if (roll <= self.get_initiative()) & (roll != 6):
                self.run = True
        else:
            self.run = False
        super().end_of_turn()

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
                if roll == 6:
                    wounds.append(0)
                elif roll >= wound_c:
                    wounds.append(ap)
        return wounds

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

