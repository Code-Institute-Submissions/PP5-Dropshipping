from django.shortcuts import render, redirect, reverse
from django.contrib import messages


from .forms import OrderForm
from shopbag.contexts import bag_contents

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KmyjjIamwSHYswF1kyZts1V2IPQWMpYe9AvlFoQYYWJWWzXKBXwmGgPN8xgcoNGJMhaNlI3iRtOtnEBNOoRFi8D00VtFyE1tr',
    }

    return render(request, template, context)