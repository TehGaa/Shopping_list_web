from django.shortcuts import render
from katalog.models import CatalogItem
context = {
    "item": CatalogItem.objects.all(),
    "nama": "Steven Yosua Saputra",
    "students_id": "2106750780"
}

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html", context)