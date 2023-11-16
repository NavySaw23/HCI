from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login_view(request):
    context = {

    }
    return render(request, 'login.html', context)


@login_required
def loggedin_view(request):
    context = {

    }
    return render(request, 'home.html', context)
