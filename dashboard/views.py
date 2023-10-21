from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.views.decorators.http import require_GET, require_POST 

# Create your views here.

@login_required
def index(request):
    # return render(request,'index1.html')
    return render(request,"master.html")

def dashboard1(request):
    return render(request,'pages/dashboard_2.html')

def content(request):
    return render(request,"pages/dashboard_2.html")

# def table(request):
#     category = Category.objects.all().values()
#     return render(request, 'pages/tables.html',{category:'category'})






