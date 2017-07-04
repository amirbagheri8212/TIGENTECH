from django.http import HttpResponse,Http404
from .models import Productseries
from django.shortcuts import render,get_object_or_404
def productpage(request):
    all_products = Productseries.objects.all()
    context = {"all_products" : all_products}
    return render(request,'Products/index.html',context)
def detail(request,Product_id):
    try:
        product=Productseries.objects.get(pk=Product_id)
        context = {"product": product,'programs':product.program_set.all()}
        return render(request, 'Products/detail.html', context)
    except:
        raise Http404("Product does Not Exist!!")
def programdetail(request,Product_id,program_id):
    product=get_object_or_404(Productseries,pk=Product_id)
    programs=product.program_set.all()
    program=programs.get(pk=program_id)
    context = {"product": product,'program':program}
    return render(request, 'Products/programdetail.html', context)
