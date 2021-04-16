from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.conf import settings
from django.utils import timezone


def save(file):
    with open(f'../talk/{file}', 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['content']
            save(file)
            return render(request, 'analysis/report.html', {'file': file})
    else:
        form = UploadFileForm()

    return render(request, 'analysis/upload.html', {'form': form})