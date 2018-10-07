from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User

from .forms import PaymentForm, PayToForm
from .models import Payments


def payments(request):
    payments = Payments.objects.all().order_by('created_date')
    return render(request, 'payments/index.html', {'payments': payments})


def payment_detail(request, id):
    payment = get_object_or_404(Payments, pk=id)
    return render(request, 'payments/detail.html', {'payment': payment})


def payment_create(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        pay_to_form = PayToForm(request.POST)

        if payment_form.is_valid() and pay_to_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.created_by_id = request.POST['user']
            payment.created_date = timezone.now()
            payment.payment_status_id = 2
            payment.payment_type_id = 1
            payment.save()

            return redirect('payments:detail', id=payment.pk)
    else:
        payment_form = PaymentForm()
        pay_to_form = PayToForm()

    return render(request, "payments/create.html", {
        'payment_form': payment_form,
        'pay_to_form': pay_to_form,
        'title': 'Pay To'})

