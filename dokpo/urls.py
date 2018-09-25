from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'', include('core.urls', namespace='core')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^payments/', include('payments.urls', namespace='payments'))
]

urlpatterns += staticfiles_urlpatterns()
