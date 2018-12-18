from django.conf.urls import url
from . import views

app_name = 'dokpo'

urlpatterns = [
    url(r'^$', views.GroupView.as_view(), name='home'),
    url(r'(?P<pk>\d+)/$', views.GroupDetail.as_view(), name='detail'),
    url(r'^create/$', views.GroupFormView.as_view(), name='create')
]