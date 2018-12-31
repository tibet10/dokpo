import django_tables2 as tables
from .models import Payments


class PaymentsTable(tables.Table):
    class Meta:
        model = Payments
        template_name = 'django_tables2/bootstrap.html'