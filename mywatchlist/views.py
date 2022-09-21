from django.shortcuts import render
from mywatchlist.models import WatchlistModel
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_watchlist(request):
    item = WatchlistModel.objects.all()

    n_no, n_yes = 0, 0
    for i in item:
        if i.watched == "YES":
            n_yes += 1
        else:
            n_no += 1

    context = {
        "nama": "Steven Yosua Saputra",
        "students_id": 2106750780,
        "item": item
    }

    if (n_yes >= n_no):
        context["selamat"] = "Selamat, kamu sudah banyak menonton!"
    else:
        context["selamat"] = "Wah, kamu masih sedikit menonton!"

    return render(request, "watchlist_index.html", context = context)

def show_json(request):
    data = WatchlistModel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = WatchlistModel.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
