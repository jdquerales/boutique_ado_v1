from django.shortcuts import redirect, render
from django.http import request
from django.urls import reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
         messages.error(request, "There's nothing in your bag at the moment")
         return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IS76KAZ4c3E746nyQUBQrYRbZMCaP2kVYIS19hmCGQQUpALiSkdtr3EpWluJhbYdcoOQbxoQ0bXk0n4n4S9p7UI00hT34AYWf',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)