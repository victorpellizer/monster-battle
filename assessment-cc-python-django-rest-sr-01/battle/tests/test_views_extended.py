from rest_framework import status

from battle.models_extended import Battle
from battle.tests.test_api_setup import BattleAPISetUp
from monster.models import Monster


class BattleAPITestsExtended(BattleAPISetUp):

    def test_battle_monster_a_wins_create(self):
        monster_a = Monster.objects.create(name="Monster A", attack=10, speed=5, defense=5,hp=20)
        monster_b = Monster.objects.create(name="Monster B", attack=5, speed=5, defense=5,hp=20)

        response = self.client.post(
            "/battle/",
            {"monsterA": monster_a, "monsterB": monster_b},
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["winner"] == monster_a

    def test_battle_monster_b_wins_create(self):
        monster_a = Monster.objects.create(
            name="Monster A",
            speed=5,
            attack=5,
            defense=5,
            hp=20)
        monster_b = Monster.objects.create(
            name="Monster B", attack=10, speed=5, 
            defense=5,hp=20)

        response = self.client.post(
            "/battle/",
            {"monsterA": monster_a, "monsterB": monster_b},
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["winner"] == monster_b

    def test_battle_invalid_monsters_dont_exist_create_return_not_found(self):
        response = self.client.post(
            "/battle/",
            {"monsterA": 9999, "monsterB": 10000},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_battle_blank_null_monsters_fail_create_return_bad_request(self):
        response = self.client.post(
            "/battle/",
            {"monsterA": None, "monsterB": ""},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_battle_successful_destroy(self):
        battle = Battle.objects.create(
            monsterA=Monster.objects.create(name="Monster A", attack=10, speed=5, defense=5,hp=20),
            monsterB=Monster.objects.create(name="Monster B", attack=5, speed=5, defense=5,hp=20),
            winner=Monster.objects.create(name="Monster A", attack=10, speed=5, defense=5,hp=20)
        )

        response = self.client.delete(f"/battle/{battle.pk}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Battle.objects.filter(pk=battle.pk).exists()

    def test_battle_fail_destroy(self):
        response = self.client.delete("/battle/9999/")

        assert response.status_code == status.HTTP_404_NOT_FOUND