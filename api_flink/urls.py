"""api_flink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from apps.credits import views
#from rest_framework.authtoken import views as restv
from rest_framework_jwt.views import obtain_jwt_token

"""router= routers.DefaultRouter()
router.register(r'credits',views.CreditViewSet)
"""


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^credits/$',views.CreditList.as_view()),# ruta de acceso a creditos
    url(r'^credits/(?P<id>[0-9]+)/$',views.CreditDetail.as_view()), # ruta de acceso solo un credito
    url(r'^credits/(?P<id>[0-9]+)/notification/(?P<type>[0-9]+)/$',views.CreditNotifications.as_view()),
   # url(r'^rest-auth/', include('rest_auth.urls')), url de autenticacion
    url(r'^api-auth/', obtain_jwt_token),# nueva url de autenticacion para token que expiran
    url(r'^credits/(?P<account>\w+)/$',views.CreditPerAccount.as_view())
]
