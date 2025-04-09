from django.contrib import admin

from .models import GameUser


@admin.register(GameUser)
class GameUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'level', 'last_completed_level', 'hp', 'money', 
                    'archer_level', 'catapult_level', 'magic_level', 'guardian_level')
    search_fields = ('username',)
