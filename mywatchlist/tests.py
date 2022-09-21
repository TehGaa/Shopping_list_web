from django.test import TestCase
from django.test import Client
from mywatchlist.models import WatchlistModel
from django.http import HttpRequest
from django.shortcuts import render

# Create your tests here.
class WatchlistTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        obj = WatchlistModel()
        obj.watched = "YES"
        obj.title = '-'
        obj.rating = 1
        obj.release_date = "-"
        obj.review = "-"
        obj.save()

    def setUp(self):
        self.html = "/mywatchlist/html"
        self.xml = "/mywatchlist/xml"
        self.json = "/mywatchlist/json"

    def test_html(self):
        print("Method: test_html")
        context = {
            "nama": "Steven Yosua Saputra",
            "students_id": 2106750780,
            "item": WatchlistModel.objects.all()
        }
        req = HttpRequest()
        req.path = self.html + "/"
        req.method = "GET"
        resp = render(req, 'watchlist_index.html', context = context)
        self.assertEqual(resp.status_code, 200)

    def test_xml(self):
        print("Method: test_xml")
        req = Client()
        resp = req.get(self.xml + '/')
        self.assertEqual(resp.status_code, 200)

    def test_json(self):
        print("Method: test_json")
        req = Client()
        resp = req.get(self.json + '/')
        self.assertEqual(resp.status_code, 200)

