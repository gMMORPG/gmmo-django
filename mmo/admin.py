"""
Django admmin management for mmo application models.
"""

from django.contrib import admin
from mmo.models import UserData, Character, World

admin.site.register(UserData)
admin.site.register(Character)
admin.site.register(World)
