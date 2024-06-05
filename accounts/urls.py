from django.urls import path
from . import views

urlpatterns = [
    path("login", views.user_login, name="login"),
    path("register", views.user_register, name="register"),
    path('logout', views.logout_view, name='logout'),
    path('profile/create', views.create_profile, name='create_profile'),
    path('profile/view', views.view_profile, name='view_profile'),   
]