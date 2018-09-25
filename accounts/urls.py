from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts.views import (
    login_view,
    register_view,
    logout_view,
    home
)

app_name = 'dokpo'

urlpatterns = [
    # url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login')
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
url(r'^register/', register_view, name='register'),
    url(r'^$', home, name='home')
]