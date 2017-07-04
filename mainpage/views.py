from django.shortcuts import render, redirect
from slider.models import sliderimg
from Quote.models import Quote
from posts.models import post
import random
def HomePage(request):
    return redirect("pagenum/1")
def HomePage1(request,pagenum):
    posts = []
    pagenum = int(pagenum)
    pagenumbers = int(len(post.objects.all()) / 3 + 1)
    pagenumbers = [i for i in range(1, pagenumbers + 1)]
    if  pagenum in pagenumbers:
        Quotes = Quote.objects.all()
        Rand_Quote = random.choice(Quotes)
        images = sliderimg.objects.all()
        if pagenum!=0:
            #1 = 0-3
            #2 = 4-7
            #3 = 8-11
            #x = (x-1)*4-(x-1)*4+3
            lastpost = (pagenum-1)*4+3
            firstpost = (pagenum-1)*4
            if firstpost<len(post.objects.all()):
                if len(post.objects.all())<lastpost:
                    lastpost = len(post.objects.all())
                posts = post.objects.all().order_by('-Publish_Time')[firstpost:lastpost]
        return render(request, 'MainPage/index.html', {"images":images, "l":images[0], "lent":[i for i in range(len(images))],"Quote": Rand_Quote, "Posts": posts,"lastpagenumber": pagenumbers,"thispage":pagenum})
    else:
        return redirect("/pagenum/1")
# Create your views here.
