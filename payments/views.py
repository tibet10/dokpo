from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import PaymentForm, ExtraFieldsForm
from .models import Payments\
    # , PayTo, ReceiveFrom
from django.contrib.auth.models import User


def home(request):
    payments = Payments.objects.all().order_by('created_date')
    return render(request, 'payments/index.html', {'payments': payments})


def payment_detail(request, id):
    payment = get_object_or_404(Payments, pk=id)
    return render(request, 'payments/detail.html', {'payment': payment})


def payment_create(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST or None)
        extra_form = ExtraFieldsForm(request.POST or None)

        if payment_form.is_valid() and extra_form.is_valid():
            # payment table
            payment = payment_form.save(commit=False)
            payment.created_by_id = request.POST['user']
            payment.created_date = timezone.now()
            payment.payment_status_id = 2
            payment.payment_type_id = 1
            payment.save()

            # extra field populating pay to
            # user = User.objects.get(id=request.POST['user'])
            # payment_type = extra_form.cleaned_data['payment_type']
            # if payment_type == 'Pay':
                # pay_to = PayTo()
                # pay_to.payment = payment
                # pay_to.user = user
                # pay_to.save()
            # else:
                # receive_from = ReceiveFrom()
                # receive_from.payment = payment
                # receive_from.user = user
                # receive_from.save()

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

