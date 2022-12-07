from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class BookTest(APITestCase):
    def test_create_book(self):
        url = reverse('restapp:books')
        data = {'booktitle': 'programming in python','bookauthor':'rossum'}
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        #self.assertEqual(response.get('data'),data)