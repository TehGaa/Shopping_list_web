from django.urls import path
from mywatchlist.views import show_json, show_watchlist, show_xml

app_name = "mywatchlist"

urlpatterns = [
    path('', show_watchlist, name = "show_watchlist"),
    path('html/', show_watchlist, name = "show_watchlist"),
    path('json/', show_json, name = "show_json"),
    path('xml/', show_xml, name = "show_xml")
]