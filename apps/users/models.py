import hashlib
import datetime
import random
from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')

        user = self.model(username=username, email=email,
                          is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(
            username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(
            username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, models.Model):

    # unique, no se van a repetir
    id_cliente = models.AutoField(primary_key=True, unique=True)
    id_authy = models.CharField(max_length=15)
    area_code = models.CharField(max_length=15)
    username = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=40)
    apaterno = models.CharField(max_length=25)
    amaterno = models.CharField(max_length=25)
    direccion = models.TextField()
    telefono = models.CharField(max_length=22)
    email = models.CharField(unique=True, max_length=30)
    genero = models.TextField()  # This field type is a guess.
    identificacion = models.ImageField(upload_to='users')
    fecha_nacimiento = models.DateField(blank=True, null=True)
    red_social = JSONField()  # This field type is a guess.
    avatar = models.ImageField()

    # intermediario entre trans de cada modelo, object managaer de cada modelo
    objects = UserManager()

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username


class UserProfile(models.Model):
    user = models.CharField(max_length=15)
    temp_pass = models.CharField(max_length=122, blank=True)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
    email = models.CharField(max_length=30)
    active = models.BooleanField(default=False)
    status = models.IntegerField()
    
    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = u'User profiles'