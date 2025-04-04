from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name = 'home-page'),
    # path('logout/', views.LogoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('update/<int:id>/', views.update_task, name='update'), 
]