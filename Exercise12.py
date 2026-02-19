# Inheridance in new classes Tank mage from character
import random
from typing import override


class Character:
    def __init__(self, name, equip):
        self.name = name
        self.health = 100 * equip.cape
        self.attack_speed = 2
        self.delay = 0
        self.max_health = 100.0 * equip.cape
        self.equipment = equip
        self.max_delay = 5
        self.attack_range = (3, 11)

    def attack(self):
        self.delay = self.max_delay - self.attack_speed
        return round(random.randrange(self.attack_range[0], self.attack_range[1]) * self.equipment.sword)

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def end_round(self):
        if self.health < 100:
            self.health += 1
        if self.delay > 0:
            self.delay -= 1

    def print(self):
        print(
            f"Character Name:{self.name},Health:{round(self.health)},Attack_Speed:{self.attack_speed},Delay:{self.delay},Equipment:{self.equipment}")

    def __str__(self):
        result = f"Name: {self.name}\nHealth:{round(self.health)}\nself.attack_speed:{self.attack_speed}\nself.delay:{self.delay}\nself.max_health:{round(self.max_health)}\nEquipment:{self.equipment}"
        return result

    def __repr__(self):
        return f"Character(name={self.name},Health={self.health},self.attack_speed={self.attack_speed},self.delay={self.delay},self.max_health={self.max_health}"

    def __iadd__(self, other):
        if isinstance(other, int):
            self.health += other
            if self.health > self.max_health:
                self.health = self.max_health
        else:
            raise ValueError(f"{other} must be INTEGER")
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            self.health -= other
            if self.health < 0:
                self.health = 0
        else:
            raise ValueError(f"{other} must be INTEGER")
        return self


class Arena:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b

    def __str__(self):
        team_a_str = "\n".join(f"  {player}" for player in self.team_a)
        team_b_str = "\n".join(f"  {player}" for player in self.team_b)

        result = (
            "===== TEAM 1 =====\n"
            f"{team_a_str}\n\n"
            "===== TEAM 2 =====\n"
            f"{team_b_str}\n"
        )
        return result

    def __repr__(self):
        return f"Arena(Team_A={self.team_a},Team_B={self.team_b}"

    def print_state(self):
        print("----TEAM A----")
        for character in self.team_a:
            character.print()
        print("----TEAM B----")
        for character in self.team_b:
            character.print()

    def play(self):
        round = 0
        while True:
            round += 1
            print(f"Round:{round}")
            avail_a = [c for c in self.team_a if c.delay == 0 and not c.is_dead()]
            avail_b = [c for c in self.team_b if c.delay == 0 and not c.is_dead()]

            alive_a = [c for c in self.team_a if not c.is_dead()]
            alive_b = [c for c in self.team_b if not c.is_dead()]

            if not alive_a and not alive_b:
                print("DRAW")
                break
            if not alive_a:
                print("TEAM B wins")
                break
            if not alive_b:
                print("TEAM A wins")
                break

            for attacker in avail_a:
                if not alive_b:
                    break
                target = random.choice(alive_b)
                dmg = attacker.attack()
                target.health = max(0, target.health - dmg)

            for attacker in avail_b:
                if not alive_a:
                    break
                target = random.choice(alive_a)
                dmg = attacker.attack()
                target.health = max(0, target.health - dmg)

            for c in self.team_a + self.team_b:
                if not c.is_dead():
                    c.end_round()


class Equipment:
    def __init__(self, sword, cape):
        if isinstance(cape, (int, float)) and isinstance(sword, (int, float)):
            if 1.1 <= sword <= 1.5 and 1.1 <= cape <= 1.3:
                self.sword = sword
                self.cape = cape
            else:
                raise ValueError(f"Sword must in range 1.1 and 1.5 and cape must be float in range 1.1 and 1.3")

        else:
            raise ValueError(f"Sword and Cape be a number")

    def __str__(self):
        return "Sword:" + str(round(self.sword, 2)) + ",Cape:" + str(round(self.cape, 2))


class Mage(Character):
    def __init__(self, name, equip):
        super().__init__(name, equip)
        self.attack_range = (8, 17)
        self.mana = 100
        self.max_mana = 100

    def end_round(self):
        super().end_round()
        if self.mana < 100:
            self.mana += 1

    @staticmethod
    def lighting_spell():
        return random.randint(30, 50)

    def attack(self):
        self.delay = self.max_delay - self.attack_speed
        if self.mana >= 55:
            self.mana -= 55
            return self.lighting_spell()
        else:
            return round(random.randint(self.attack_range[0], self.attack_range[1]) * self.equipment.sword)


class Tank(Character):
    def __init__(self, name, equip):
        super().__init__(name, equip)
        self.attack_range = (20, 30)
        self.max_health = self.max_health * 2
        self.health = self.max_health


total_equipments = []
for i in range(10):
    eq = Equipment(random.uniform(1.1, 1.5), random.uniform(1.1, 1.3))
    total_equipments.append(eq)
orc1 = Character("Ntope", total_equipments[0])
orc2 = Tank("Vlassonio", total_equipments[1])

orc4 = Character("Skoulikion", total_equipments[3])
orc5 = Character("Valmadin", total_equipments[4])

night_elf1 = Character("Crowly", total_equipments[5])
night_elf2 = Character("Hydra", total_equipments[6])
night_elf3 = Character("Sodapopin", total_equipments[7])
night_elf4 = Mage("Xoverdose", total_equipments[2])
team_a = [orc1, orc2, orc4, orc5]
team_b = [night_elf1, night_elf2, night_elf3, night_elf4]
arena1 = Arena(team_a, team_b)

arena1.print_state()
arena1.play()
arena1.print_state()
