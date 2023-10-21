from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.views.decorators.http import require_GET, require_POST
# Create your views here.


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

def signup(request):
    form = UserCreationForm() 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
        else:
            form = UserCreationForm() 
    return render(request,'user/signup.html',context={'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request,'user/login.html')

def profile(request):
    return render(request,'user/profile.html')
