from django.urls import reverse

from rest_framework import status

from monster.models import Monster
from monster.tests.test_api_setup import MonsterAPISetUp
import os


class MonsterAPITestsExtended(MonsterAPISetUp):
    
    def get_csv_file_path(self, filename):
        """Helper to get CSV file from media folder"""
        base_path = os.path.join(os.path.dirname(__file__), "..", "..", "media")
        return os.path.join(base_path, filename)

    def test_monster_successful_import(self):
        """Test importing a valid CSV file"""
        csv_file_path = self.get_csv_file_path("monsters-correct.csv")
        
        with open(csv_file_path, "rb") as csv_file:
            response = self.client.post(
                "/monster/import/",
                {"file": csv_file},
                format="multipart",
            )

        assert response.status_code == status.HTTP_201_CREATED
        assert Monster.objects.count() > 0

    def test_monster_empty_import(self):
        """Test importing an empty CSV file"""
        csv_file_path = self.get_csv_file_path("monsters-empty-monster.csv")
        
        with open(csv_file_path, "rb") as csv_file:
            response = self.client.post(
                "/monster/import/",
                {"file": csv_file},
                format="multipart",
            )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_monster_wrong_import(self):
        """Test importing a CSV file with invalid data"""
        csv_file_path = self.get_csv_file_path("monsters-wrong-column.csv")
        
        with open(csv_file_path, "rb") as csv_file:
            response = self.client.post(
                "/monster/import/",
                {"file": csv_file},
                format="multipart",
            )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
