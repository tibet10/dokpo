from django import forms
from django.contrib.auth.models import User
from .models import Payments, PaymentType, PaymentStatus, Groups


class PaymentForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    amount = forms.DecimalField(
        required=True
    )
    details = forms.Textarea()

    payment_type = forms.ModelChoiceField(
        queryset=PaymentType.objects.only('name'),
        required=True,
        empty_label="Select Payment Type"
    )

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=True,
        empty_label="Select User"
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.group = kwargs.pop('group', None)
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['details'].required = False

    class Meta:
        model = Payments
        fields = ['payment_type', 'user', 'subject', 'amount', 'details']

    def save(self, *args, **kwargs):
        payment = super(PaymentForm, self).save(commit=False)
        # current_group = Groups.objects.get(pk=1)
        payment.payment_status = PaymentStatus.objects.filter(name='Pending')[0]
        payment.payment_type = self.cleaned_data.get('payment_type')
        payment.created_by = self.user
        payment.group = self.group
        payment.save()
        return payment




