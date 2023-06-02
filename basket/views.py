from django.shortcuts import render


# Create your views here.
def view_basket(request):
    """
    A view to render the basket/basket.html page
    """
    return render(request, 'basket/basket.html')
