from django.db import models
from monster.models import Monster
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Battle(models.Model):
    monsterA = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Monster A",
        related_name="battle_monster_a",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    monsterB = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Monster B",
        related_name="battle_monster_b",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    winner = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Winner",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    class Meta:
        verbose_name = "Battle"
        verbose_name_plural = "Battles"
        ordering = ["id"]
