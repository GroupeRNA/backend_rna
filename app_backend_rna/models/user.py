from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, user_name, user_mail,  user_password=None):
        if not user_name:
            raise ValueError("Le Nom d'Utilisateur est obligatoire")
        if not user_mail:
            raise ValueError("L'email est obligatoire")
        
        user = self.model(
            user_name=user_name,
            user_mail=self.normalize_email(user_mail)
        )
        user.set_password(user_password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_name, user_mail, user_password):
        user = self.create_user(
            user_name=user_name,
            user_mail=user_mail,
            user_password=user_password
        )

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=150, unique=True)
    user_mail = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['user_mail']

    def __str__(self):
        return self.user_name