from django.urls import path
from mywatchlist.views import show_watchlist, show_xml, show_json, show_watched_films

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watched_films, name='show_watched_films'),
    path('html/', show_watchlist, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]