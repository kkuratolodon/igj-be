from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone


class GameUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class GameUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    display_name = models.CharField(max_length=50, default="Player", null=False, blank=False)
    
    # Game progress
    last_completed_level = models.IntegerField(default=0)
    tutorial_complete = models.BooleanField(default=False)
    
    # Player resources
    hp = models.IntegerField(default=100)
    money = models.IntegerField(default=200)
    
    # Unit upgrade levels
    archer_level = models.IntegerField(default=1)
    catapult_level = models.IntegerField(default=1)
    magic_level = models.IntegerField(default=1)
    guardian_level = models.IntegerField(default=1)
    
    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = GameUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['display_name']
    
    def __str__(self):
        return self.username
