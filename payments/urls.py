from django.conf.urls import url
from . import views

app_name = 'dokpo'

urlpatterns = [
    url(r'^$', views.payments, name='home'),
    url(r'(?P<id>\d+)/$', views.payment_detail, name='detail'),
    url(r'^create/$', views.payment_create, name='create')
]