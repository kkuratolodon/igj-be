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
    # Game progress
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    last_completed_level = models.IntegerField(default=0)
    
    # Player resources
    hp = models.IntegerField(default=100)
    money = models.IntegerField(default=1000)
    
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
    
    def __str__(self):
        return self.username
