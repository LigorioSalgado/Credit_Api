from apps.credits.models import Credit
from apps.accounts.models import Account
from rest_framework  import serializers

class CreditSerializer(serializers.ModelSerializer):
	class Meta:
		model = Credit
		fields = ('id_credito', 'monto','interes','fecha_in','fecha_fin','total','status','plazo') 

