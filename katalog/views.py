from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(req):
    return render(req, "katalog.html", context)

item_data = CatalogItem.objects.all()
context = {
    'item_list': item_data,
    'nama': 'Fresty',
    'npm': '2106750742'
}