from monster.models import Monster


# Create your battle Algorithm here
def fight(monster_a: Monster, monster_b: Monster) -> Monster:
    attacker, defender = get_attack_order(monster_a, monster_b)
    # print(f"Estou aqui na briga entre {attacker.name} e {defender.name}")
    while attacker.hp > 0 and defender.hp > 0:
        damage = attacker.attack - defender.defense
        if damage <= 0:
            damage = 1
        
        defender.hp -= damage
        if defender.hp <= 0:
            break

        # swap roles for next turn
        attacker, defender = defender, attacker

    winner = attacker if defender.hp <= 0 else defender
    # print(f"E o vencedor é {winner.name}")
    return winner

def get_attack_order(monster_a: Monster, monster_b: Monster):
    if monster_a.speed > monster_b.speed:
        return monster_a, monster_b
    elif monster_a.speed < monster_b.speed:
        return monster_b, monster_a
    else:
        a_is_stronger = monster_a.attack >= monster_b.attack
        attacker = monster_a if a_is_stronger else monster_b
        defender = monster_b if a_is_stronger else monster_a
        return attacker, defender
