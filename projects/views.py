from django.shortcuts import render
from .models import Project
from login.models import User

# Create your views here.
def id_view(request, gal_id):
    obj = Project.objects.get(id=gal_id)
    context = {
        'obj':obj
    }
    return render(request, 'id.html', context)

# @login_required
def id_view_logged(request, gal_id, user_id):
    obj = Project.objects.get(id=gal_id)
    user = User.objects.get(id=user_id)
    context = {
        'obj' : obj,
        'user' : user
    }
    return render(request, 'id.html', context)

# def like(request, gal_id, user_id):
#     obj = Project.objects.get(id=gal_id)
#     user = User.objects.get(id=user_id)
    
#     obj.like_count += 1
    
#     if gal_id == 1:
#         user.Hasliked1 = True

#     obj.save()

#     context = {
#         'obj' : obj,
#         'user' : user
#     }
#     return render(request, 'id.html', context)