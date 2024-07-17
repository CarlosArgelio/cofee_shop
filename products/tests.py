from django.test import TestCase
from django.urls import reverse


class ProductListViewTest(TestCase):

    def test_should_return_200_when_load_page(self):
        url = reverse("list_product")

        response = self.client.get(url)
        status_code = response.status_code

        self.assertEqual(status_code, 200)
