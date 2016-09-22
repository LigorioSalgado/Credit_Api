from django.shortcuts import render
from apps.credits.models import Credit
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apps.credits.serializers import CreditSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import requests
from django.http import Http404


class CreditList(APIView):



    def get(self, request, format=None):  # obtiene  peticion get si esta  autentificado
        credits = Credit.objects.all()
        serializer = CreditSerializer(credits, many=True)
        return Response(serializer.data)


class CreditDetail(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self,request,id, format=None):

        print request.data
        r = requests.post("http://api.webhookinbox.com/i/O5HUtRbE/in/",json=request.data)

        return Response({"message":"ok","action":"datos contratos"}, status.HTTP_202_ACCEPTED)


class CreditNotifications(APIView):

    def post(self,request,id,type,format=None):
        print type

        if type == '1':
            print request.data
            r = requests.post("http://api.webhookinbox.com/i/O5HUtRbE/in/", json=request.data)
            return Response({"message":"ok", "action":"notificacion deposito"},status=status.HTTP_200_OK)
        elif type == '2':
            print request.data
            r = requests.post("http://api.webhookinbox.com/i/O5HUtRbE/in/", json=request.data)
            return Response({"message": "ok", "action": "notificacion pago"}, status=status.HTTP_200_OK)

        else:
            print request.data
            r = requests.post("http://api.webhookinbox.com/i/O5HUtRbE/in/", json=request.data)
            return Response({"message": "error", "detail": "tipo de notificacion no especificado"}, status=status.HTTP_400_BAD_REQUEST)

"""
    def delete(self, request, pk, format=None):
        	credit = self.get_object(pk)
       		 credit.delete()
        	return Response(status=status.HTTP_204_NO_CONTENT)
"""


class CreditPerAccount(APIView):


    def get_object(self, account):
        try:
            return Credit.objects.get(cuenta=account)
        except Credit.DoesNotExist:
            raise Http404

    def get(self, request, account):
        credit = self.get_object(account)
        serializer = CreditSerializer(credit)
        return Response(serializer.data)
