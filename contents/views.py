from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from os.path import splitext






def home(request):
    
    return render(request, 'contents/portfolio.html')



