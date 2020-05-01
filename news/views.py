from django.shortcuts import render, redirect

from news.models import HeadLine
from news.scraper import BaseScraper


def scrape(request):
    for ChildClass in BaseScraper.__subclasses__():
        scraper = ChildClass()
        scraper.scrape()
    return redirect('../')


def news_list(request):
    headlines = HeadLine.objects.all().order_by("-pk")
    context = {
        'object_list': headlines
    }
    return render(request, 'news/home.html', context)
