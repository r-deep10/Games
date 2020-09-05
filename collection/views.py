from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from collection.models import Games, Feedback
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def trend(request):
    return render(request, 'trending.html', {})

def all(request):
    games = Games.objects.all()
    return render(request,'all_games.html',{'games': games})


def index(request):
    user_list = Games.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    return render(request, 'front.html', {'games': games})


def game(requests):
    return render(requests, 'front.html', {})
    

def fetch(requests, gameid):
    got = get_object_or_404(Games, game_id=gameid)
    return render(requests, 'detail.html', {'got': got})


def filt(request, general):
    fit = Games.objects.filter(category__contains=general)

    content = {"games": fit}
    return render(request, 'all_games.html', content)


def abc4(request):
    return render(request, 'about.html', {})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')

        if query is not None:
            lookups = Q(gname__contains=query) | Q(
                category__contains=query)

            results = Games.objects.filter(lookups).distinct()

            context = {'results': results}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')


def feedback(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        country = request.POST['country']
        comment = request.POST['comment']

        feed = Feedback(firstname=firstname, lastname=lastname,
                        country=country, comment=comment)
        feed.save()
        messages.info(request, 'Thank You, for your feedback!')

        return render(request, 'feedback.html', {})

    else:
        return render(request, 'feedback.html', {})

