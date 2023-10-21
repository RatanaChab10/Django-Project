from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from .models import Category
from django.core.exceptions import RequestAborted
from django.views.decorators.http import require_GET , require_POST 

# Create your views here.


# def my_view(request):
#     category = Category.objects.all()
#     return render(request, 'pages/tables.html', {'category':category})

@require_GET
def view_table(request):
    categorys = Category.objects.all()
    
    return render(request,'pages/tables.html',{'categorys':categorys})

@require_GET
def create(request):
    if request.user.is_authenticated:
        return render(request,'category/create.html')
    else:
        messages.success(request,"No Permission")
        return redirect('/view_table')
    
@require_GET
def view_category(request,id):
    if request.user.is_authenticated:
        category_record = Category.objects.get(id=id)
        return render(request,'category/view.html',{'category_record':category_record})
    else:
        messages.success(request,"No Permission")
        return redirect('/view_table')

@require_POST
def store(request):
    try:
        category = Category()
        category.name = request.POST["name"]
        category.create_by = 1
        category.save()
        messages.success(request,"Category Created.")
        return redirect('/view_table')
    except Exception as e:
        print("Error:" + str(e))
        
    return render(request,'pages/tables.html')


@require_GET
def edit(request,id):    
    category_record = Category.objects.get(id=id)
    return render(request,'category/update.html',{'category_record':category_record})

@require_POST
def category_update(request,id):
    if request.user.is_authenticated:
        category_record = Category(id=id)
        category_record.name = request.POST["name"]
        category_record.create_by = 1
        category_record.save()
        messages.success(request,"Category Updated.")
        return redirect('/view_table')
    else:
        messages.success(request,"No Permission")
    return redirect('/view_table')

def category_delete(request,id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('/view_table')
    else:
        messages.success(request,"No Permission")
    return redirect('/view_table')