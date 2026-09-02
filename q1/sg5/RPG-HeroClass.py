# ============================================================
# hi sir :)
# ============================================================

class Hero:
    def __init__(self, name, hp):
        # Store `name` and `hp` as INSTANCE attributes
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        # Subtract `amount` from this hero's hp
        self.hp -= amount


# ------------------------------------------------------------
# hi again sir
# ------------------------------------------------------------
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

# Arthur takes 10 damage
arthur.take_damage(10)

print(arthur.hp)     # Expected: 90
print(morgana.hp)    # Expected: 100
