from django.test import TestCase
from restaurant.models import menu
from restaurant.serializers import menuSerializer
import json


class MenuViewTest(TestCase):
   # Use the setup() method to add a few test instances of the Menu model.
    def setUp(self):
        self.item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = menu.objects.create(title="Cake", price=100, inventory=100)

    #add another test_getall() instance method to retrieve all the Menu objects added for the test purpose. 
    def test_getall(self):
        #The retrieved objects must serialized, so make sure the method runs assertions to check if the serialized data equals the response.
        items = menu.objects.all()
        serializer = menuSerializer(items, many=True)
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')
        self.assertEqual(response.get('Content-Type'), 'application/json')
        self.assertEqual(response.status_code, 200)     
        self.assertEqual(json.loads(response.content), serializer.data)

        
