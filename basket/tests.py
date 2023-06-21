from django.test import TestCase
from products.models import Product


# Create your tests here.
class TestBasketViews(TestCase):

    def test_get_basket_page(self):
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_add_product_to_basket(self):
        product = Product.objects.create(
            sku='12334',
            name='Test Product',
            description='This is the description for a test product',
            price=99.99,
            has_sizes=False,
            rating=5,
        )

        response = self.client.post(
            f'/basket/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_basket'}
        )
        basket = self.client.session['basket']
        self.assertEqual(basket[str(product.id)], 1)

    def test_remove_product_from_basket(self):
        product = Product.objects.create(
            sku='12334',
            name='Test Product',
            description='This is the description for a test product',
            price=99.99,
            has_sizes=False,
            rating=5,
        )
        self.client.post(
            f'/basket/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_basket'}
        )
        response = self.client.post(f'/basket/remove/{product.id}/')
