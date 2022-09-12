from django.shortcuts import render
from katalog.models import CatalogItem


# TODO: Create your views here.
def show_katalog(request):
    context = {
        "item": CatalogItem.objects.all(),
        "nama": "Steven Yosua Saputra",
        "students_id": "2106750780"
    }
    return render(request, "katalog.html", context)