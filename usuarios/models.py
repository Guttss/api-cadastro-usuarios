from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Adicione o related_name para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set', # Nome exclusivo
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True   
    )


class ManageUser(BaseUserManager):
    def create_user(self, email, password, name):
        if email is None:
            raise ValueError('O usuario precisa ter um e-mail válido')
        #Criaçao do usuario
        user = self.model(email=email, name=name)
        user.set_password(password) #Criptografando a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name, is_superuser=True, is_staff=True):
        super_user = self.create_user(email, password, name)

        # Defina atributos de superusuario
        super_user.is_superuser = is_superuser
        super_user.is_staff = is_staff

        super_user.save(using=self._db)
        return super_user

