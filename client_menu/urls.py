from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns =[
    path('', views.HomeView.as_view(), name='home_view'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
]
