from django.shortcuts import render
from mywatchlist.models import WatchlistModel
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_watchlist(request):
    item = WatchlistModel.objects.all()
    context = {
        "nama": "Steven Yosua Saputra",
        "students_id": 2106750780,
        "item": item
    }
    return render(request, "watchlist_index.html", context = context)

def show_json(request):
    data = WatchlistModel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = WatchlistModel.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
