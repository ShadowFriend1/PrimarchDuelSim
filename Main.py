from Alpharius import Alpharius
from Angron import Angron, BentAngron
from Corax import CoraxDeath, CoraxScourge, CoraxShadow
from FerrusManus import FerrusManus
from Fulgrim import FulgrimLaer, FulgrimFireblade
from Horus import HorusWorldBreaker, HorusTalon
from Khan import KhanAfoot, KhanMounted
from KonradCurze import KonradCurze
from Leandros import LeandrosBlade, LeandrosShield
from LemanRuss import LemanRussBalenight, LemanRussHelwinter
from Lion import LionWolf, LionSword
from Lorgar import Lorgar, LorgarEmpowered
from Magnus import Magnus, MagnusIronArm, MagnusEndurance, MagnusWarpSpeed, MagnusAllBiomancy, MagnusPrecognition
from Mortarion import Mortarion
from Perturabo import Perturabo, PerturaboHammer
from Primarch import Primarch
from RobouteGuilliman import RobouteGuillimanHand, RobouteGuillimanGladius
from RogalDorn import RogalDorn
from Sanguinius import SanguiniusBlade, SanguiniusSpear, SanguiniusMoonsilver
from Sydek import SydekAbyss, SydekDriver
from Vulkan import Vulkan


def shoot_fight(ff: Primarch, sf: Primarch):
    ff_shoot = ff.shoot(sf.get_shoot_hit_mod(), sf.get_shoot_wound_mod(), sf.get_toughness(),
                        sf.get_fleshbane_tough(), sf.get_fleshbane_immune(), sf.get_dorn(), False)
    sf_dead = sf.save(ff_shoot[0], ff_shoot[1], ff_shoot[2], False, False, True, False, ff_shoot[3], ff_shoot[4])
    if sf_dead:
        # print(ff.get_name()+" wins with: "+str(ff.get_wounds())+" wounds remaining")
        return 1
    sf_shoot = sf.shoot(ff.get_shoot_hit_mod(), ff.get_shoot_wound_mod(), ff.get_toughness(),
                        ff.get_fleshbane_tough(), ff.get_fleshbane_immune(), ff.get_dorn(), True)
    ff_dead = ff.save(sf_shoot[0], sf_shoot[1], sf_shoot[2], False, False, False, False, sf_shoot[3], sf_shoot[4])
    if ff_dead:
        # print(sf.get_name()+" wins with: "+str(sf.get_wounds())+" wounds remaining")
        return 2
    return 0


def impact_fight(ff, sf):
    ff_impact = ff.impact(sf.get_wound_mod(), sf.get_toughness(), sf.get_dorn())
    sf_dead = sf.save(ff_impact, False, False, False, False, False, False, False, False)
    if sf_dead:
        if sf.get_initiative() >= 10:
            sf_fight = sf.fight(ff.get_hit_mod(), ff.get_wound_mod(), ff.get_weapon_skill(), ff.get_toughness(),
                                ff.get_fleshbane_tough(), ff.get_fleshbane_immune(), ff.get_initiative(), ff.get_dorn())
            ff_dead = ff.save(sf_fight[0], sf_fight[1], sf_fight[2], sf_fight[3], sf_fight[4], False, sf_fight[5],
                              False, False)
            if ff_dead:
                # print("The fight is a draw with simultaneous deaths")
                return 3
            else:
                # print(ff.get_name()+" wins with: "+str(ff.get_wounds())+" wounds remaining")
                return 1
        else:
            # print(ff.get_name()+" wins with: "+str(ff.get_wounds())+" wounds remaining")
            return 1
    else:
        return 0


def fight(ff: Primarch, sf: Primarch, simultaneous):
    ff_fight = ff.fight(sf.get_hit_mod(), sf.get_wound_mod(), sf.get_weapon_skill(), sf.get_toughness(),
                        sf.get_fleshbane_tough(), sf.get_fleshbane_immune(), sf.get_initiative(), sf.get_dorn())
    sf_dead = sf.save(ff_fight[0], ff_fight[1], ff_fight[2], ff_fight[3], ff_fight[4], False, ff_fight[5],
                      False, False)
    if sf_dead & (not simultaneous):
        # print(ff.get_name()+" wins with: "+str(ff.get_wounds())+" wounds remaining")
        return 1
    sf_fight = sf.fight(ff.get_hit_mod(), ff.get_wound_mod(), ff.get_weapon_skill(), ff.get_toughness(),
                        ff.get_fleshbane_tough(), ff.get_fleshbane_immune(), ff.get_initiative(), ff.get_dorn())
    ff_dead = ff.save(sf_fight[0], sf_fight[1], sf_fight[2], sf_fight[3], sf_fight[4], False, sf_fight[5],
                      False, False)
    if sf_dead & ff_dead:
        # print("The fight is a draw with simultaneous deaths")
        return 3
    elif ff_dead:
        if (sf.get_initiative() == 1) & (servo_fight(ff, sf) == 3):
            print(3)
            # print("The fight is a draw with simultaneous deaths")
            return 3
        # print(sf.get_name()+" wins with: "+str(sf.get_wounds())+" wounds remaining")
        return 2
    elif sf_dead:
        if (simultaneous & (ff.get_initiative() == 1)) & (servo_fight(ff, sf) == 3):
            # print("The fight is a draw with simultaneous deaths")
            return 3
        # print(ff.get_name()+" wins with: "+str(ff.get_wounds())+" wounds remaining")
        return 1
    else:
        return 0


def servo_fight(ff: Primarch, sf: Primarch):
    ff_dead = False
    sf_dead = False
    if ff.get_servo():
        ff_fight = ff.servo_fight(sf.get_hit_mod(), sf.get_wound_mod(), sf.get_weapon_skill(), sf.get_toughness(),
                                  sf.get_dorn())
        sf_dead = sf.save(ff_fight[0], ff_fight[1], ff_fight[2], ff_fight[3], ff_fight[4], False, False, False, False)
    if sf.get_servo():
        sf_fight = sf.servo_fight(ff.get_hit_mod(), ff.get_wound_mod(), ff.get_weapon_skill(), ff.get_toughness(),
                                  ff.get_dorn())
        ff_dead = ff.save(sf_fight[0], sf_fight[1], sf_fight[2], sf_fight[3], sf_fight[4], False, False, False, False)
    if sf_dead & ff_dead:
        # print("The fight is a draw with simultaneous deaths")
        return 3
    elif sf_dead:
        # print(ff.get_name()+" wins with: "+str(ff.get_wounds())+" wounds remaining")
        return 1
    elif ff_dead:
        # print(sf.get_name()+" wins with: "+str(sf.get_wounds())+" wounds remaining")
        return 2
    else:
        return 0


if __name__ == "__main__":
    simulations = 10000
    fulgrim_laer = FulgrimLaer()
    fulgrim_fireblade = FulgrimFireblade()
    rogal_dorn = RogalDorn()
    konrad_curze = KonradCurze()
    ferrus_manus = FerrusManus()
    angron = Angron()
    bent_angron = BentAngron()
    roboute_guilliman_gladius = RobouteGuillimanGladius()
    roboute_guilliman_hand = RobouteGuillimanHand()
    mortarion = Mortarion()
    horus_hammer = HorusWorldBreaker()
    horus_talon = HorusTalon()
    lorgar = Lorgar()
    lorgar_empowered = LorgarEmpowered()
    vulkan = Vulkan()
    corax_death = CoraxDeath()
    corax_scourge = CoraxScourge()
    corax_shadow = CoraxShadow()
    alpharius = Alpharius()
    leman_russ_sword = LemanRussBalenight()
    leman_russ_axe = LemanRussHelwinter()
    magnus = Magnus()
    magnus_iron_arm = MagnusIronArm()
    magnus_endurance = MagnusEndurance()
    magnus_warp_speed = MagnusWarpSpeed()
    magnus_all_biomancy = MagnusAllBiomancy()
    magnus_precognition = MagnusPrecognition()
    sanguinius_encarmine = SanguiniusBlade()
    sanguinius_spear = SanguiniusSpear()
    sanguinius_moonsilver = SanguiniusMoonsilver()
    khan_afoot = KhanAfoot()
    khan_mounted = KhanMounted()
    lion_wolf = LionWolf()
    lion_sword = LionSword()
    perturabo = Perturabo()
    pert_hammer = PerturaboHammer()
    leandros_blade = LeandrosBlade()
    leandros_shield = LeandrosShield()
    sydek_abyss = SydekAbyss()
    sydek_driver = SydekDriver()
    # primarchs = [fulgrim_fireblade, fulgrim_laer, rogal_dorn, konrad_curze, ferrus_manus, angron, bent_angron,
    #              roboute_guilliman_gladius, roboute_guilliman_hand, mortarion, horus_hammer, horus_talon, lorgar,
    #              lorgar_empowered, vulkan, corax_death, corax_scourge, corax_shadow, alpharius, leman_russ_axe,
    #              leman_russ_sword, magnus, magnus_endurance, magnus_iron_arm, magnus_warp_speed, magnus_all_biomancy,
    #              magnus_precognition, sanguinius_spear, sanguinius_encarmine, sanguinius_moonsilver, khan_afoot,
    #              khan_mounted, lion_sword, lion_wolf, perturabo, pert_hammer, leandros_blade, leandros_shield,
    #              sydek_abyss, sydek_driver]
    final_results = {}
    for N in reversed(primarchs):
        fighter_a = N
        primarchs.remove(N)
        for M in primarchs:
            fighter_b = M
            result_set = []
            if fighter_a.get_type() != fighter_b.get_type():
                x = 0
                while x < 2:
                    i = 0
                    while i < (simulations/2):
                        fighter_a.reset(1)
                        fighter_b.reset(2)
                        finished = 0
                        final = 0
                        while finished == 0:
                            if fighter_a.get_run():
                                finished = shoot_fight(fighter_a, fighter_b)
                                if finished == 0:
                                    finished = impact_fight(fighter_a, fighter_b)
                            elif fighter_b.get_run():
                                finished = shoot_fight(fighter_b, fighter_a)
                                if finished == 0:
                                    finished = impact_fight(fighter_b, fighter_a)
                            if (fighter_a.get_asf() & (not fighter_b.get_asf())) & (finished == 0):
                                finished = fight(fighter_a, fighter_b, False)
                                final = 1
                            elif (fighter_b.get_asf() & (not fighter_a.get_asf())) & (finished == 0):
                                finished = fight(fighter_b, fighter_a, False)
                                final = 2
                            elif (fighter_a.get_initiative() > fighter_b.get_initiative()) & (finished == 0):
                                finished = fight(fighter_a, fighter_b, False)
                                final = 1
                            elif (fighter_a.get_initiative() < fighter_b.get_initiative()) & (finished == 0):
                                finished = fight(fighter_b, fighter_a, False)
                                final = 2
                            elif finished == 0:
                                finished = fight(fighter_a, fighter_b, True)
                            if finished == 0:
                                finished = servo_fight(fighter_a, fighter_b)
                            if finished == 0:
                                fighter_a.end_of_turn()
                                fighter_b.end_of_turn()
                        results = []
                        if finished == 1:
                            if final == 2:
                                results = [fighter_b.get_name(), fighter_a.get_name(), "Win"]
                            else:
                                results = [fighter_a.get_name(), fighter_b.get_name(), "Win"]
                        elif finished == 2:
                            if final == 2:
                                results = [fighter_a.get_name(), fighter_b.get_name(), "Win"]
                            else:
                                results = [fighter_b.get_name(), fighter_a.get_name(), "Win"]
                        else:
                            results = [fighter_a.get_name(), fighter_b.get_name(), "Draw"]
                        result_set.append(results)
                        i += 1
                    temp = fighter_a
                    fighter_a = fighter_b
                    fighter_b = temp
                    x += 1
            for result in result_set:
                display = result[0] + " " + result[2] + " Against " + result[1]
                display2 = result[1] + " Draw Against " + result[0]
                if display in final_results:
                    final_results[display] += 1
                    if (display2 in final_results) & (result[2] == "Draw"):
                        final_results[display2] = final_results[display]
                elif (result[2] == "Draw") & (display2 in final_results):
                    final_results[display2] += 1
                    final_results[display] = final_results[display2]
                else:
                    final_results[display] = 1
    for x in sorted(final_results):
        print('%80s %5s' % (x + ": ", str(round((final_results[x] / simulations) * 100, 2)) + "%"))