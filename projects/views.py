from django.shortcuts import render
from .models import Project
from login.models import User
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def all_view(request):
    obj = Project.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'all.html', context)


def id_view(request, gal_id):
    obj = Project.objects.get(id=gal_id)
    context = {
        'obj': obj
    }
    return render(request, 'id.html', context)


def registrationView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['confirm_password']:
                obj = form.save(commit=False)
                obj.set_password(obj.password)
                obj.save()
                messages.success(request, 'You have been registered.')
                return redirect('login')
            else:
                return render(request, "registration.html", {'form': form, 'note': 'password must match'})
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {'form': form})


def loginView(request):
    if request.method == "POST":
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=usern, password=passw)
        if user is not None:
            login(request, user)
            return redirect('gal')
        else:
            messages.success(request, 'Invalid username or password!')
            return render(request, "login.html")
    else:
        return render(request, "login.html")


@login_required
def logoutView(request):
    logout(request)
    return redirect('gal')

# # @login_required
# def id_view_logged(request, gal_id, user_id):
#     obj = Project.objects.get(id=gal_id)
#     user = User.objects.get(id=user_id)
#     context = {
#         'obj' : obj,
#         'user' : user
#     }
#     return render(request, 'id.html', context)

@login_required
def like(request, gal_id):
    obj = Project.objects.get(id=gal_id)
    user = request.user
    obj.like_count += 1

    if gal_id == 1:
        user.Hasliked1 = True

    obj.save()

    context = {
        'obj' : obj,
    }
    return render(request, 'id.html', context)
