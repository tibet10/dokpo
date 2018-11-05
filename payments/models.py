from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from groups.models import Groups


class PaymentStatus(models.Model):
    APPROVED = 'A'
    PENDING = 'P'
    STATUS_CODE = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved')
    )
    name = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=10, choices=STATUS_CODE, null=False, default=PENDING)

    def __str__(self):
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

    def __str__(self):
        return self.name


class Payments(models.Model):
    subject = models.CharField(max_length=255, null=False, default='')
    details = models.TextField(max_length=500, null=True, blank=True)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    payment_type = models.ForeignKey(PaymentType, null=False, on_delete=models.DO_NOTHING)
    payment_status = models.ForeignKey(PaymentStatus, null=False, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, null=True, related_name="payments_created_by", on_delete=models.DO_NOTHING)
    users = models.ManyToManyField(User, through='PaymentMembership')
    group = models.ForeignKey(Groups, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.subject

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class PaymentMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now, null=True, blank=True)
    payment_type = models.ForeignKey(PaymentType, null=False, on_delete=models.DO_NOTHING)





