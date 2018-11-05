from django import forms
from .models import Groups, GroupMembership, MemberStatus


class GroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Add group name..'
        }
    ), required=True, label='Group Name')

    details = forms.CharField(widget=forms.Textarea(), required=False, label="Details")

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

    def save(self, user, *args, **kwargs):
        group = super(GroupForm, self).save(commit=False)
        group.name = self.cleaned_data['name']
        group.details = self.cleaned_data['details']
        group.created_by = user
        group.save()
        return group

    class Meta:
        model = Groups
        fields = ['name', 'details']


class ExtraFieldForm(forms.Form):
    email_1 = forms.EmailField(label='Email 1', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Add email..'
        }
    ), required=False)

    email_2 = forms.EmailField(label='Email 2', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Add email..'
        }
    ), required=False)

    email_3 = forms.EmailField(label='Email 3', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Add email..'
        }
    ), required=False)
