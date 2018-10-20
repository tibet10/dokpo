from django.shortcuts import render


def home(request):
    context = {'title': 'Dhrogpo', 'Description': 'Tashi Delek!! Welcome to pay to friend site.'}
    return render(request, 'core/index.html', context)
