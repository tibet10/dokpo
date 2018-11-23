from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Groups(models.Model):
    name = models.CharField(max_length=255, null=False)
    details = models.TextField(max_length=500, null=True, blank=True)
    created_by = models.ForeignKey(User, null=False, related_name='group_created_by', on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    members = models.ManyToManyField(User, through='GroupMembership', related_name='group_members')

    def __str__(self):
        return self.name

    def payment_id(self):
        return self.payment.values_list('id', flat=True).first()


class MemberStatus(models.Model):
    APPROVED = 'A'
    DENIED = 'D'
    PENDING = 'P'
    STATUS_CODE = (
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
        (PENDING, 'Pending')
    )
    name = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=10, choices=STATUS_CODE, null=False, default=PENDING)
    created_date = models.DateTimeField(default=timezone.now, null=True, blank=True)


class GroupMembership(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, null=False, on_delete=models.CASCADE)
    member_status = models.ForeignKey(MemberStatus, null=False, on_delete=models.DO_NOTHING)
    date_joined = models.DateTimeField(default=timezone.now, null=True, blank=True)
