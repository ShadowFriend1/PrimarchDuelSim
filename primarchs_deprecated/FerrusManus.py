import random

from primarchs_deprecated.Primarch import Primarch


class FerrusManus(Primarch):
    name = "Ferrus Manus"
    ws = 7
    bs = 6
    s = 10
    t = 7
    i = 5
    a = 4
    inv = 3
    ap = 1
    concussive = True
    type = 10
    servo = True
    gun_ap = 2
    gun_str = 7
    shots = 2
    shoot_wound_mod = -1

    def shoot(self, shoot_hit_mod, shoot_wound_mod, e_t, fp_t, fp_i, dorn, overwatch):
        if overwatch:
            wound = self.wound(random.randint(1, 3), 5, shoot_wound_mod, e_t, fp_t, fp_i, dorn, 4, False)
        else:
            wound = self.wound(1, 5, shoot_wound_mod, e_t, fp_t, fp_i, dorn, 4, False)
        hits = self.shoot_hit(self.get_ballistic_skill(), shoot_hit_mod, self.shots)
        return self.shoot_wound(hits, self.gun_str, shoot_wound_mod, e_t, fp_t, fp_i, dorn, self.gun_ap,
               self.fp_w_gun) + wound, self.gun_concussive, self.gun_blinding & hits > 0, \
               self.deflagrate, self.soul_blaze
