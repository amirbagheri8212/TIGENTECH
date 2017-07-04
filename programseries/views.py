from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Program_Serie
#def index(request):
#    programseries=Program_Serie.objects.all()
#    return render(request,"programseries/index.html",{'programseriesvalue':programseries})
def productpage(request):
    all_programseries = Program_Serie.objects.all()
    if all_programseries:
        context = {"all_programseries": all_programseries}
        return render(request,'programseries/index.html',context)

    return render(request,'NotFound.html',{'ERTEXT':"Database Connection Problem Program Series Not Found"})
def detail(request,Product_id):
    try:
        product=Program_Serie.objects.get(pk=Product_id)
        programs = product.program_set.all()
        if programs:
            context = {"product": product,'programs':programs}
            return render(request, 'programseries/detail.html', context)
        return render(request, 'NotFound.html', {'ERTEXT':"Database Connection Problem Program for {Name} Not Found".format(Name=product.Title)})
    except:
        return render(request, 'NotFound.html', {'ERTEXT':"This Program serie does not seem to be on our Database"})
def programdetail(request,Product_id,Program_id):
    product=get_object_or_404(Program_Serie,pk=Product_id)
    programs=product.program_set.all()
    program=programs.get(pk=Program_id)
    context = {"product": product,'program':program}
    return render(request, 'programseries/programdetail.html', context)









