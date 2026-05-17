from django.urls import reverse

from rest_framework import status

from monster.models import Monster
from monster.tests.test_api_setup import MonsterAPISetUp


class MonsterAPITestsExtended(MonsterAPISetUp):
    
    def test_monster_successful_import(self):
           #TODO
        assert False, "Not implemented"
        
    def test_monster_empty_import(self):
           #TODO
        assert False, "Not implemented"
        
    def test_monster_wrong_import(self):
           #TODO
        assert False, "Not implemented"
        
