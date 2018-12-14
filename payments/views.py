from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm
from .models import Payments, PaymentStatus, PaymentType, PaymentMembership
from groups.models import Groups
from django.views.generic import TemplateView, DetailView, CreateView, FormView


class PaymentsView(TemplateView):
    template_name = 'payments/index.html'

    def get_payment(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            payments = Payments.objects.all().order_by('created_date')
        else:
            payments = Payments.objects.filter(group_id=pk).order_by('created_date')
        return payments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payments'] = self.get_payment()
        return context


class PaymentDetail(DetailView):
    model = Payments
    template_name = 'payments/detail.html'
    context_object_name = 'payment'


class PaymentFormView(FormView):
    template_name = "payments/create.html"
    form_class = PaymentForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(PaymentFormView, self).get_form_kwargs()
        if self.request.user:
            kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        group_id = self.kwargs.get('group_id')
        group = get_object_or_404(Groups, pk=group_id)
        context = super().get_context_data(**kwargs)
        context['payment_form'] = PaymentForm(self.request.POST or None)
        context['title'] = 'Add New Payment'
        context['group'] = group
        return context

    def form_valid(self, form):
        payment = form.save()
        # first member
        payment_membership_first = PaymentMembership()
        payment_membership_first.user = payment.created_by
        payment_membership_first.payment_type = form.cleaned_data['payment_type']
        payment_membership_first.payment = payment
        payment_membership_first.save()

        # second member
        payment_membership_second = PaymentMembership()
        payment_membership_second.user = form.cleaned_data['user']
        other_type = PaymentType.objects.all().exclude(pk=payment_membership_first.payment_type.pk)[0]
        payment_membership_second.payment_type = other_type
        payment_membership_second.payment = payment
        payment_membership_second.save()

        return redirect('payments:detail', pk=payment.pk)

