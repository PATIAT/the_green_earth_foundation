from django.test import TestCase
from .models import Category, Product
from django.contrib.auth.models import User
from django.test.client import Client


# Create your tests here.
class TestProductViews(TestCase):

    def test_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_add_product_page_for_user(self):
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    def test_get_add_product_page_for_admin(self):
        # Create a test super user
        password = 'concoweijcosdifpwefdj23'
        superuser = User.objects.create_superuser(
            'SuperUser1',
            'testemail@email.com',
            password
        )
        self.client.login(username=superuser.username, password=password)

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed((response, 'products/add_product.html'))


class TestProductModels(TestCase):

    def test_string_representation(self):
        product = Product(name="Test Product Name")
        self.assertEqual(str(product), product.name)

    def test_category_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "Categories")
