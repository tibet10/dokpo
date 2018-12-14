from django.shortcuts import render, redirect, get_object_or_404
from .forms import GroupForm
from .models import Groups, GroupMembership, MemberStatus
from django.views.generic import TemplateView, DetailView,FormView
from core.utils.mixins import LoginRequiredMixin


class GroupView(LoginRequiredMixin, TemplateView):
    template_name = 'groups/index.html'

    def groups(self):
        self.is_not_used()
        groups = Groups.objects.all()
        return groups

    def is_not_used(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = self.groups()
        context['description'] = 'Welcome to groups'
        return context


class GroupDetail(LoginRequiredMixin, DetailView):
    model = Groups
    template_name = 'groups/detail.html'
    context_object_name = 'group'


class GroupFormView(LoginRequiredMixin, FormView):
    template_name = "groups/create.html"
    form_class = GroupForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(GroupFormView, self).get_form_kwargs()
        if self.request.user:
            kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(GroupFormView, self).get_context_data(**kwargs)
        context['title'] = 'Add New Group'
        return context

    def form_valid(self, form):
        group = form.save()
        group_member = GroupMembership()
        group_member.group = group
        group_member.user = group.created_by
        group_member.member_status = MemberStatus.objects.filter(name='Approved')[0]
        group_member.save()
        return redirect('groups:detail', pk=group.pk)

