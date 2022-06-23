from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

from web.models import Category, News


def index(request):

    categories = Category.objects.all()
    top_menu = Category.objects.all() [:8]
    trending = News.objects.all() [:5]
    entertinement = News.objects.filter(categories=2) [:5]
    education = News.objects.filter(categories=1) [:5]

    news = News.objects.all()

    search_categories = request.GET.get("category")
    print(search_categories)
    if search_categories:
        news = news.filter(categories__in=search_categories)

    instances = Paginator(news, 5)
    page = request.GET.get("page", 1)

    try:
        instances = instances.page(page)
    except PageNotAnInteger:
        instances = instances.page(1)
    except EmptyPage:
        instances = instances.page(instances.num_pages)


    context = {
        "categories": categories,
        "instances": instances,
        "top_menu": top_menu,
        "trending": trending,
        "entertinement":entertinement,
        "education": education
    }
    return render(request, "index.html", context=context)


def news(request, id):
    categories = Category.objects.all()
    top_menu = Category.objects.all() [:8]
    trending = News.objects.all() [:5]
    entertinement = News.objects.filter(categories=2) [:5]
    education = News.objects.filter(categories=1) [:5]
    search_categories = request.GET.get("category")
    print(search_categories)
    if search_categories:
        news = news.filter(categories__in=search_categories)
    instances = get_object_or_404(News.objects.filter(id=id))

    context = {
        "categories": categories,
        "top_menu": top_menu,
        "trending": trending,
        "entertinement": entertinement,
        "education": education,
        "instances": instances,
    }
    return render(request, "news.html", context=context)