from django.db import models
from apps.users.models import User

class Account(models.Model):
    no_cuenta = models.CharField(primary_key=True, max_length=8)
    historial = models.TextField()
    punt_game = models.IntegerField()
    propietario = models.OneToOneField(User)
    friend = models.TextField()

   

    class Meta:
        managed = False
        db_table = 'accounts_account'