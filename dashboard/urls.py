from django.urls import path
from . import views as view1, user, category,product
from django.contrib.auth import views as auth_view
# from . import category

urlpatterns = [
    path('',view1.index,name='index'),
    path('dashboard1/',view1.dashboard1,name='dashboard1'),
    path('content/',view1.content,name='content'),
    # path('tables/',view1.table,name='table'),
    
    path('create/',category.create,name='category_create'),
    path('store/',category.store,name='store'),
    path('view_table/',category.view_table,name='view_table'),
    path('view_record/<int:id>',category.view_category,name='view_record'),
     path('edit/<int:id>',category.edit,name='edit_record'),
    path('update_record/<int:id>',category.category_update,name="category_update"),
    path('delete/<int:id>/', category.category_delete, name='category_delete'),
    
    # product controller 
    path('product_table/',product.index,name='product_table'),
    path('product_table/create',product.create,name='product_create'),
    path('store_product/',product.store_product,name='store_product'),
    path('view_product/<int:id>',product.view_product,name='view_product'),
    path('edit_product/<int:id>',product.edit_product,name='edit_product'),
    path('update_product/<int:id>',product.update_product,name='update_product'),
    
    
    # User Form
    path('sign_up/',user.signup,name='sign_up'),
    path('login/',auth_view.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='user/login.html'),name='logout'),
    path('profile/',user.profile,name='profile'),
]
