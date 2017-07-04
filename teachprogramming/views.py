from django.shortcuts import render
from django.http import Http404,HttpResponse
from .models import programlanguages
from django.shortcuts import render,get_object_or_404
def index(request):
    all_languages = programlanguages.objects.all()
    context = {"all_languages": all_languages}
    return render(request, 'Teach/index.html', context)
def teach(request,Language):
    languages = programlanguages.objects.get(pk=Language)
    programs = languages.program_set.all()
    context = {"Language":programs}
    return render(request,'Teach/Tutorial List.html',context)
def TTutorial(request,Language,TUT):
    languages = programlanguages.objects.get(pk=Language)
    programs = languages.program_set.all()
    program= programs.get(pk=TUT)
    context = {"program": program}
    return render(request, 'Teach/tutorialview.html', context)
