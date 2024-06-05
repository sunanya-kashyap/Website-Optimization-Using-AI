from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Website, File, OptimizedFile, Log, Feedback, Report
from .forms import *

def Addwebsite(request):
    form = WebsiteForm()
    if request.method == 'POST':
        form = WebsiteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Website added successfully!')
        return redirect('dashboard')
    return render(request, 'addwebsite.html', {'form': form})


def viewwebsite(request, id):
    website = Website.objects.get(id=id)
    return render(request, 'viewwebsite.html', {'website': website})

def dashboard(request):
    websites = Website.objects.all()
    return render(request, 'dashboard.html', {'websites': websites})

import zipfile
import os
import shutil
def optimized(request, id):

    website = Website.objects.get(id=id)
    website.optimization_status = 'In progress'
    website.save()
    # unzip the zip file
    zip_file = zipfile.ZipFile(website.zip_file.path, 'r')
    zip_file.extractall(f'media/{website.name}')
    zip_file.close()
    # get all files in the unzipped folder
    for root, folder, files in os.walk(f'media/{website.name}'):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_type = file_path.split('.')[-1]
                website_file = File(file=file_path, size=file_size, file_type=file_type, website=website)
                website_file.save()
            except Exception as e:
                print(e)

    # unzip files store them in files table
    website_files = File.objects.filter(website=website)
    messages.success(request, 'All files extracted')
    return render(request, 'optimized.html', {'website': website, 'files': website_files})



def Feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Feedback = Feedback(name=name, email=email, message=message)
        Feedback.save()
        return render(request, 'Feedback.html', {'message': 'Feedback sent successfully!'})
    else:
        return render(request, 'Feedback.html')
    
def report(request):
    reports = Report.objects.all()
    return render(request, 'report.html', {'reports': reports})

def viewlog(request):
    logs = Log.objects.all()
    return render(request, 'log_view.html', {'logs': logs})

def viewfile(request):
    files = File.objects.all()
    return render(request, 'file_view.html', {'files': files})

def viewoptimizedfile(request):
    optimizedfiles = OptimizedFile.objects.all()
    return render(request, 'optimizedfile_view.html', {'optimizedfiles': optimizedfiles})

def delete_website(request, id):
    website = Website.objects.get(id=id)
    website.delete()
    messages.success(request, 'Website deleted successfully!')
    return redirect('dashboard')


def add_website(request):
    # Code to add website...

    return redirect('optimized?success=true')

def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            number = request.POST.get('number')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact = contact(name=name,number=number, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, 'Message sent')
            return redirect('home')
        except:
            messages.error(request, 'Error sending message')
    return render(request, 'contact.html')

def download_files(request):
    # Replace 'path_to_file' with the actual path to the file you want to download
    path_to_file = '/path'
    FileResponse = FileResponse(open(path_to_file, 'rb'))
    return FileResponse