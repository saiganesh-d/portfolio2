from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from os.path import splitext
from .models import (Certification, Education, Focus, ProfessionalSkill,
                     Profile, Project, ProjectCategory, Recommendation,
                     Seminar, TechnicalSkill, WorkExperience)


def certification(request, pk):
    file = get_object_or_404(Certification, pk=pk)
    file_path = str(file.document)
    file_type = ''

    try:
        # Get the file extension:
        extension = splitext(file_path[16:])[1]
        if extension == '.pdf':
            file_type = 'application/pdf'

        response = FileResponse(open(f'media/{file_path}', 'rb'), content_type=file_type)
        response['Content-Disposition'] = f'filename={file_path[16:]}'

        return response
    except FileNotFoundError:
        raise Http404()


def home(request):
    
    return render(request, 'contents/portfolio.html')



