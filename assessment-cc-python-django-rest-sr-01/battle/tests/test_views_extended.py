from django.urls import reverse

from rest_framework import status

from battle.models_extended import Battle
from battle.tests.test_api_setup import BattleAPISetUp


class BattleAPITestsExtended(BattleAPISetUp):
    
    def test_battle_monster_a_wins_create(self):
        #TODO
        assert False, "Not implemented"
        
    def test_battle_monster_b_wins_create(self):
        #TODO
        assert False, "Not implemented"

    def test_battle_invalid_monsters_dont_exist_create_return_not_found(self):
        #TODO
        assert False, "Not implemented"
    
    def test_battle_blank_null_monsters_fail_create_return_bad_request(self):
        #TODO
        assert False, "Not implemented"

    def test_battle_successful_destroy(self):
        #TODO
        assert False, "Not implemented"
    
    def test_battle_fail_destroy(self):
        #TODO
        assert False, "Not implemented"
