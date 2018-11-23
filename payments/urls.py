from django.conf.urls import url
from . import views

app_name = 'dokpo'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^group/(?P<id>\d+)/$', views.payment_grp_id, name='group'),
    url(r'(?P<id>\d+)/$', views.payment_detail, name='detail'),
    url(r'^create/$', views.payment_create, name='create')
]