from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'dokpo'

urlpatterns = [
    url(r'^$', views.PaymentsView.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', views.PaymentDetail.as_view(), name='detail'),
    url(r'^group/(?P<pk>\d+)/$', views.PaymentsView.as_view(), name='group'),
    url(r'^create/(?P<group_id>\d+)/$', views.PaymentFormView.as_view(), name='create')
]