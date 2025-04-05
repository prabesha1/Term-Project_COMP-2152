class KingAura:
    def __init__(self, hero_strength, monster_strength, monster_hp, belt):
        self.hero_strength = hero_strength
        self.monster_strength = monster_strength
        self.monster_hp = monster_hp
        self.belt = belt

    def can_activate(self):
        return self.hero_strength >= 8 and (
            "King’s Will" in self.belt or "Emperor's Cape" in self.belt
        )

    def activate(self):
        if not self.can_activate():
            return "No effect"

        if self.monster_strength <= 3 or self.monster_hp <= 3:
            self.monster_hp = 0
            return "Monster fainted from King's pressure"
        elif 4 <= self.monster_strength <= 6:
            self.monster_strength //= 2
            return "Monster weakened, strength halved"
        else:
            return "Monster resisted the King's aura"

    def get_updated_stats(self):
        return self.monster_strength, self.monster_hp
