from rest_framework import serializers

from monster.models import Monster
from battle.models_extended import Battle
from battle.utils_extended import fight
from monster.nested_serializers_extended import MonsterListRetrieveUpdateSerializer

class BattleListSerializer(serializers.ModelSerializer):
    monsterA = MonsterListRetrieveUpdateSerializer()
    monsterB = MonsterListRetrieveUpdateSerializer()
    winner = MonsterListRetrieveUpdateSerializer()

    class Meta:
        model = Battle
        fields = "__all__"


class BattleCreateSerializer(serializers.ModelSerializer):
    monsterA = serializers.IntegerField()
    monsterB = serializers.IntegerField()
    winner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Battle
        fields = "__all__"

    def validate(self, attrs):
        monsterA = attrs.get("monsterA")
        monsterB = attrs.get("monsterB")

        if monsterA == monsterB:
            raise serializers.ValidationError(
                "monsterA and monsterB must be different monsters."
            )

        if not Monster.objects.filter(pk=monsterA).exists():
            raise serializers.ValidationError({"monsterA": "Monster A does not exist."})

        if not Monster.objects.filter(pk=monsterB).exists():
            raise serializers.ValidationError({"monsterB": "Monster B does not exist."})

        return attrs

    def create(self, validated_data):
        monster_a = Monster.objects.get(pk=validated_data["monsterA"])
        monster_b = Monster.objects.get(pk=validated_data["monsterB"])
        winner = fight(monster_a, monster_b)
        validated_data["winner"] = winner.pk

        return Battle.objects.create(**validated_data)
