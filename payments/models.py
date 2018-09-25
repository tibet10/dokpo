from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PaymentStatus(models.Model):
    APPROVED = 'A'
    PENDING = 'P'
    STATUS_CODE = (
        (PENDING, 'Pending'),
        (APPROVED,'Approved')
    )
    name = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=10, choices=STATUS_CODE, null=False, default=PENDING)

    def __unicode__(self):
        return self.name


class PaymentType(models.Model):
    PAY = 'P'
    RECEIVE = 'R'
    TYPE_CODE = (
        (PAY, 'Pay'),
        (RECEIVE, 'Receive')
    )
    name = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=10, choices=TYPE_CODE, null=False, default=PAY)

    def __unicode__(self):
        return self.name


class Payments(models.Model):
    subject = models.CharField(max_length=255, null=False, default='')
    details = models.TextField(max_length=500, null=True, blank=True)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    payment_type = models.ForeignKey(PaymentType, null=False, on_delete=models.DO_NOTHING)
    payment_status = models.ForeignKey(PaymentStatus, null=False, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class PayTo(models.Model):
    payment = models.ForeignKey(Payments, null=False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.payment.title


class ReceiveFrom(models.Model):
    payment = models.ForeignKey(Payments, null=False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.payment.title




