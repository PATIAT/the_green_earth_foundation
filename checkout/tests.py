from django.test import TestCase
from .forms import OrderForm


# Create your tests here.
class TestCheckoutViews(TestCase):

    def test_get_checkout_with_empty_basket(self):

        response = self.client.get('/checkout')
        self.assertTrue(response, '/products')


class TestCheckoutForm(TestCase):
    def test_checkout_form_fields_required(self):
        form_data = {
            'full_name': '',
            'email': '',
            'phone_number': '',
            'street_address1': '',
            'town_or_city': '',
            'country': '',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)
        self.assertListEqual(
            list(form.errors.keys()),
            [
                'full_name',
                'email',
                'phone_number',
                'street_address1',
                'town_or_city',
                'country',
            ],
        )
        for field in form.errors:
            self.assertEqual(
                form.errors[field][0], 'This field is required.'
            )

    def test_checkout_form_valid_data(self):
        form_data = {
            'full_name': 'Test Name',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Street',
            'town_or_city': 'Anytown',
            'country': 'GB',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())
