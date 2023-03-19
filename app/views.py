from django.shortcuts import render

# Create your views here.


def static_generic(request):
    return render(request,'static_generic.html')