from django.shortcuts import render

# Create your views here.
def all_view(request):
    context = {

    }
    return render(request, 'all.html', context)