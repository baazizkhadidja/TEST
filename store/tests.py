from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import Appart, Program, Caract


#Index page
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


#detail test item exits
class DetailPageTestCase(TestCase):

    def setUp(self):
        impossible = Appart.objects.create(title="Transmission impossible")
        self.app = Appart.objects.get(title='Transmission Impossible')





def test_new_booking_is_registred(self):
        old_apps = Appart.objects.count()
        app_id = self.app.id
        response = self.client.post(reverse('store:detail',
        args=[app_id]
        new_apps = Appart.objects.count()
        self.assertEqual(new_apps, old_apps + 1 )