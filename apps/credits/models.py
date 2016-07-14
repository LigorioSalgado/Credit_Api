from django.db import models
from apps.accounts.models import Account

class Credit(models.Model):
    id_credito = models.AutoField(primary_key=True)
    monto = models.FloatField()
    interes = models.FloatField()
    t_interes = models.FloatField()
    fecha_in = models.DateTimeField()
    fecha_fin = models.DateField()
    fecha_real = models.DateField(blank=True, null=True)
    ponderacion = models.TextField()
    status = models.IntegerField()
    cuenta = models.ForeignKey(Account,related_name='Account', null=True)
    plazo = models.IntegerField()
    total = models.FloatField()
    pago_diario = models.FloatField(blank=True, null=True)
    lista_dias = models.CharField(max_length=900, blank=True, null=True)
    """
    class Meta:
        managed = False
        db_table = 'credits_credit'
   """
    def serialize_hook(self,hook):
    	return{
    		'hook':hook.dict(),
    		'data':{
				'id_credito': self.id_credito,
    			'monto': self.monto,
    			'fecha_inicio': self.fecha_in,
    			'fecha_final': self.fecha_fin,
    			'status': self.status

    		}
    	}

	
    
