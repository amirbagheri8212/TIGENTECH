from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Item
from Quote.models import Quote
import random
def mainp(request):
    return redirect("pagenum/1")
def page(request,pagenum):
    pageItems = []
    pagenum = int(pagenum)
    Quotes = Quote.objects.all()
    Rand_Quote = random.choice(Quotes)

    if pagenum!=0:
        # 1 = 0-20
        # 2 = 21-41
        # 3 = 42-62
        # x = (x-1)*21-(x-1)*21+20
        allitems = Item.objects.all()

        lastitem = (pagenum - 1) * 21 + 20
        firstitem = (pagenum - 1) * 21
        if firstitem<len(allitems):
            if len(allitems)<lastitem:
                lastitem = len(allitems)
            pageItems = allitems.order_by('-Publish_Time')[firstitem:lastitem]
    return render(request,"Store/index.html",{"Items":pageItems,"Quote": Rand_Quote})