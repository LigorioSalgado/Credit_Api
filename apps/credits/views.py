from django.shortcuts import render
from apps.credits.models import Credit
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.credits.serializers import CreditSerializer
from rest_framework import status, permissions
from apps.credits.permissions import ApiUserPermission
from rest_framework_expiring_authtoken.authentication import ExpiringTokenAuthentication
from django.http import Http404

class CreditList (APIView):
	permission_classes = (ApiUserPermission,)# clase  de permisos especiales "permissions.py"
	authentication_classes = (ExpiringTokenAuthentication,)
	def get(self,request,format=None):#obtiene  peticion get si esta  autentificado
		credits=Credit.objects.all()
		serializer = CreditSerializer(credits, many=True)
		return Response(serializer.data)


class CreditDetail(APIView):
	authentication_classes = (ExpiringTokenAuthentication,)
	def get_object(self, pk): #metodo que busca la primary key del credito, cuando falla lanza  error 404 al usuario
		try:
			return Credit.objects.get(pk=pk)
		except Credit.DoesNotExist:
			raise Http404

    	def get(self, request, pk, format=None): # get especifico para el credito 
		credit = self.get_object(pk)
		serializer = CreditSerializer(credit)
		return Response(serializer.data)

    	def patch(self, request, pk, format=None):# methodo patch (verbo http parecido a PUT) con la finalidad de modificar ciertos campos del credito y no todo el objeto
		credit  = self.get_object(pk)
		serializer = CreditSerializer(credit, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # si falla lanza un bad request al usuario  error 403
"""
    def delete(self, request, pk, format=None):
        	credit = self.get_object(pk)
       		 credit.delete()
        	return Response(status=status.HTTP_204_NO_CONTENT)
"""

class CreditPerAccount(APIView):
	permission_classes = (ApiUserPermission,)	
	authentication_classes = (ExpiringTokenAuthentication,)	

	def get_object(self,account):
		try:
			return  Credit.objects.get(cuenta=account)
		except Credit.DoesNotExist:
			raise Http404
	
	def get(self, request, account):
		credit = self.get_object(account)
		serializer=CreditSerializer(credit)
		return Response(serializer.data)
