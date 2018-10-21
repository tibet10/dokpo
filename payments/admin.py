from django.contrib import admin
from .models import Payments, PaymentStatus, PaymentType, PaymentMembership

admin.site.register(Payments)
admin.site.register(PaymentStatus)
admin.site.register(PaymentType)
admin.site.register(PaymentMembership)
