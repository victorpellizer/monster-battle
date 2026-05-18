from django.db import models
from monster.models import Monster
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Battle(models.Model):
    monsterA = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Monster A",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    monsterB = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Monster B",
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
