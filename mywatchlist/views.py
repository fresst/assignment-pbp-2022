from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
# global var
data_watchlist = MyWatchList.objects.all()

def show_watchlist(req):
    context = {
        'films' : data_watchlist,
        'nama' : 'Fresty',
        'npm' : '2106750742'
    }
    return render(req, "mywatchlist.html",context)

def show_watched_films(req):
    context = {
        'films' : data_watchlist,
        'nama' : 'Fresty',
        'status' : string_watched()
    }
    return render(req, "watchedfilms.html", context)

def show_xml(req):
    return HttpResponse(serializers.serialize("xml", data_watchlist), 
                        content_type="application/xml")

def show_json(req):
    return HttpResponse(serializers.serialize("json", data_watchlist), 
                        content_type="application/json")

def string_watched():
    watched_count = MyWatchList.objects.filter(watched=True).count()
    if(watched_count >= data_watchlist.count()//2):
        return "Selamat, kamu sudah banyak menonton!"
    else:
        return "Wah, kamu masih sedikit menonton!"