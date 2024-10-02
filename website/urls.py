from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    # path('login/', views.login_user , name = 'login_user'),
    path('logout/', views.logout_user , name = 'logout_user'),
    path('register/', views.register_user , name = 'register'),
    path('records/<int:pk>', views.customer_records , name = 'records'),
    path('delete_records/<int:pk>', views.delete_records , name = 'delete_records'),
     path('add_record/', views.add_record , name = 'add_record'),
     path('update_record/<int:pk>', views.update_record , name = 'update_record'),
]
