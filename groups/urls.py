from django.conf.urls import url
from . import views

app_name = 'dokpo'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'(?P<id>\d+)/$', views.group_detail, name='detail'),
    url(r'^create/$', views.group_create, name='create')
]