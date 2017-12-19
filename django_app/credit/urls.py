from django.conf.urls import url

from credit.serializer import CreditSerializer

urlpatterns = [
    url(r'^list/$', CreditSerializer.as_view(), name='credit_list'),
]