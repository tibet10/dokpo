from django.contrib import admin
from .models import Payments, PaymentStatus, PaymentType

admin.site.register(Payments)
admin.site.register(PaymentStatus)
admin.site.register(PaymentType)
