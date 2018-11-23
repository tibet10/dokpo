from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm, ExtraFieldsForm
from .models import Payments, PaymentStatus, PaymentType, PaymentMembership, Groups
from django.contrib.auth.models import User


def home(request):
    payments = Payments.objects.all().order_by('created_date')
    return render(request, 'payments/index.html', {'payments': payments})


def payment_detail(request, id):
    payment = get_object_or_404(Payments, pk=id)
    return render(request, 'payments/detail.html', {'payment': payment})


def payment_grp_id(request, id):
    payments = Payments.objects.filter(group_id=id).order_by('created_date')
    return render(request, 'payments/index.html', {'payments': payments})


def payment_create(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST or None)
        extra_form = ExtraFieldsForm(request.POST or None)

        if payment_form.is_valid() and extra_form.is_valid():
            extra_data = extra_form.cleaned_data
            current_group = Groups.objects.get(pk=1)
            payment = payment_form.save(user=request.user, p_t=extra_data['payment_type'], c_g=current_group)

            # first member
            payment_membership_first = PaymentMembership()
            payment_membership_first.user = request.user
            payment_membership_first.payment_type = extra_data['payment_type']
            payment_membership_first.payment = payment
            payment_membership_first.save()

            # second member
            payment_membership_second = PaymentMembership()
            payment_membership_second.user = extra_data['user']
            other_type = PaymentType.objects.all().exclude(pk=payment_membership_first.payment_type.pk)[0]
            payment_membership_second.payment_type = other_type
            payment_membership_second.payment = payment
            payment_membership_second.save()

        return redirect('payments:detail', id=payment.pk)
    else:
        payment_form = PaymentForm()
        extra_form = ExtraFieldsForm()

    context = {
        'payment_form': payment_form,
        'extra_form': extra_form,
        'title': 'Add New Payment'
    }
    return render(request, "payments/create.html", context)

