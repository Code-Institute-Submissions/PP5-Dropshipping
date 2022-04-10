from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from shopbag.contexts import bag_contents

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KmyjjIamwSHYswF1kyZts1V2IPQWMpYe9AvlFoQYYWJWWzXKBXwmGgPN8xgcoNGJMhaNlI3iRtOtnEBNOoRFi8D00VtFyE1tr',
    }

    return render(request, template, context)