from django.shortcuts import render, redirect, get_object_or_404
from .forms import GroupForm, ExtraFieldForm
from .models import  Groups, GroupMembership, MemberStatus


def home(request):
    return render(request, 'groups/index.html', {'description': 'Welcome to groups' })


def group_detail(request, id):
    group = get_object_or_404(Groups, pk=id)
    return render(request, "groups/detail.html", {'group': group})


def group_create(request):
    if request.method == 'POST':
        group_form = GroupForm(request.POST or None)
        extra_form = ExtraFieldForm(request.POST or None)
        if group_form.is_valid() and extra_form.is_valid():
            group = group_form.save(user=request.user)

            group_member = GroupMembership()
            group_member.group = group
            group_member.user = request.user
            group_member.member_status = MemberStatus.objects.filter(name='Approved')[0]
            group_member.save()

            return redirect('groups:detail', id=group.pk)
    else:
        group_form = GroupForm()
        extra_form = ExtraFieldForm()

    context = {
        'group_form': group_form,
        'extra_form': extra_form,
        'title': 'Add New Group'
    }
    return render(request, "groups/create.html", context)
