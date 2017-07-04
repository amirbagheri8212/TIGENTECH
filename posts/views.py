from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import post,genre
from Quote.models import Quote

import random
# Create your views here.
def mainp(request):
    return redirect("/")
def postdet(request,genrepk,postpk):
    Post = post.objects.all().get(pk=postpk)
    Quotes = Quote.objects.all()
    Rand_Quote = random.choice(Quotes)
    return render(request, 'Posts/Postview.html',
                  {"Quote": Rand_Quote,"Post":Post})
def genredet(request, genrepk):
    Genre = genre.objects.get(pk=genrepk)
    all_posts = Genre.post_set.all()
    Quotes = Quote.objects.all()
    Rand_Quote = random.choice(Quotes)
    return render(request, 'Posts/Genreview.html', {"Quote": Rand_Quote, "Genre":Genre, "Posts":all_posts})