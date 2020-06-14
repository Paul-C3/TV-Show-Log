from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import TVshows

def newshowform (request):
    return TemplateResponse(request, 'add_newshow.html')

def process (request):
    context = {'name': request.POST['name'], 'network': request.POST['network'], 'releasedate': request.POST['releasedate'], 'description': request.POST['description']}
    tvshow = TVshows(title = context.name)
    tvshow.save()
    return TemplateResponse(request, 'add_newshow.html')
# Create your views here.
