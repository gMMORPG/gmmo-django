"""
Models for mmo application.
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserData(models.Model):
    """
    Model for store user additional data.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    character = models.ManyToManyField("Character", related_name="user_characters", blank=True)

    class Meta:
        verbose_name = "User data"
        verbose_name_plural = "Users data"

    def __str__(self):
        return f"#{self.id} - {self.user.username}'s data"


class Character(models.Model):
    """
    Model for store character data.
    """

    name = models.CharField(max_length=50)
    skin = models.CharField(max_length=50)
    direction_x = models.DecimalField(max_digits=5, decimal_places=2)
    direction_y = models.DecimalField(max_digits=5, decimal_places=2)
    position_x = models.DecimalField(max_digits=5, decimal_places=2)
    position_y = models.DecimalField(max_digits=5, decimal_places=2)
    world = models.ForeignKey("World", related_name="character_world", on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        return f"#{self.id} - {self.name}"


class World(models.Model):
    """
    Model for store world data.
    """

    SAFE = "safe"
    PVP = "pvp"
    ANY_OTHER = "any_other"

    MORAL_CHOICES = [
        (SAFE, "Safe"),
        (PVP, "PvP"),
        (ANY_OTHER, "Any other"),
    ]

    name = models.CharField(max_length=50)
    moral = models.CharField(max_length=50, choices=MORAL_CHOICES, default=SAFE)
    size_x = models.DecimalField(max_digits=5, decimal_places=2)
    size_y = models.DecimalField(max_digits=5, decimal_places=2)
    characters = models.ManyToManyField("Character", related_name="characters_in_world", blank=True)

    class Meta:
        verbose_name = "World"
        verbose_name_plural = "Worlds"

    def __str__(self):
        return f"#{self.id} - {self.name}"
