from audioop import reverse
import imp
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class UrlTestCase(TestCase):
    client = Client()
    
    def test_url_html(self):
        """Test URL mywatchlist/html"""
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_url_xml(self):
        """Test URL mywatchlist/xml"""
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_url_json(self):
        """Test URL mywatchlist/json"""
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)