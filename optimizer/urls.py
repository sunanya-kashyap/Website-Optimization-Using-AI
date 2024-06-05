from django.urls import path
from . import views

urlpatterns = [

    path('dashboard', views.dashboard, name='dashboard'),
    # create website
    path('Addwebsite', views.Addwebsite, name='Addwebsite'),
    # view website
    path('viewwebsite/<int:id>', views.viewwebsite, name='viewwebsite'),
    # optimize website
    path('optimize/<int:id>', views.optimized, name='optimized'),
    # delete website
    path('delete/<int:id>', views.delete_website, name='delete_website'),
    # contact
    path('contact', views.contact_view, name='contact'),
    # download files
    path('download_files/', views.download_files, name='download_files'),
    # Feedback
    path('Feedback', views.Feedback_view, name='Feedback'),
 ]