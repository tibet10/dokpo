from django import forms
from django.contrib.auth.models import User
from .models import Payments, PaymentType, PaymentStatus


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

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['details'].required = False

    class Meta:
        model = Payments
        fields = ['subject', 'amount', 'details']

    def save(self, user, p_t,c_g,*args, **kwargs):
        payment = super(PaymentForm, self).save(commit=False)
        payment.payment_status = PaymentStatus.objects.filter(name='Pending')[0]
        payment.payment_type = p_t
        payment.created_by = user
        payment.group = c_g
        payment.save()
        return payment


class ExtraFieldsForm(forms.Form):
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


