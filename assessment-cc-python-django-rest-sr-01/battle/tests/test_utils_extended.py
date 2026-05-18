from monster.models import Monster

from battle.tests.test_utils_setup import UtilsSetUp
from battle.utils_extended import fight


def add_monsters(monster_a, monster_b):
    monster_list = [Monster(**row) for row in [monster_a, monster_b]]

    Monster.objects.bulk_create(monster_list)


class UtilsTests(UtilsSetUp):
    def setUp(self):
        super().setUp()

    def test_monster_with_equal_speed_and_monster_a_higher_attack_fight(self):
        add_monsters(
            {"name": "Monster A", "attack": 10, "speed": 5, "defense": 10, "hp": 20},
            {"name": "Monster B", "attack": 5, "speed": 5, "defense": 10, "hp": 20},
        )

        monster_a = Monster.objects.get(name="Monster A")
        monster_b = Monster.objects.get(name="Monster B")

        winner = fight(monster_a, monster_b)

        assert getattr(winner, "pk", winner) == monster_a.pk

    def test_monster_with_equal_speed_and_monster_b_higher_attack_fight(self):
        add_monsters(
            {"name": "Monster A", "attack": 5, "speed": 5, "defense": 10, "hp": 20},
            {"name": "Monster B", "attack": 10, "speed": 5, "defense": 10, "hp": 20},
        )

        monster_a = Monster.objects.get(name="Monster A")
        monster_b = Monster.objects.get(name="Monster B")

        winner = fight(monster_a, monster_b)

        assert getattr(winner, "pk", winner) == monster_b.pk