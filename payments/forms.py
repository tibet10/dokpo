from django import forms
from django.contrib.auth.models import User
from .models import Payments, PaymentType


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

# class PayToForm(forms.ModelForm):
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(),
#         required=True,
#         empty_label="Select User"
#     )
#     class Meta:
#         model = PayTo
#         fields = ['user']


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


