from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import CartItem
from django.contrib.auth.decorators import login_required
from services.models import Service
from payments.forms import MakePaymentForm
from django.template.context_processors import csrf
from django.contrib import messages
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET



@login_required(login_url="/accounts/login")
def user_cart(request):
    cartItems = CartItem.objects.filter(user=request.user)
    total = 0
    for item in cartItems:
        total += item.quantity * item.service.price

    if request.method == 'POST':
        form = MakePaymentForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                CartItem.objects.filter(user=request.user).delete()
                return redirect(reverse('all_services'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        if len(cartItems) == 0:
            return render(request, 'empty_cart.html')

        form = MakePaymentForm()

    args = {'form': form,
            'items': cartItems,
            'total': total,
            'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'cart.html', args)




@login_required(login_url="/accounts/login")
def add_to_cart(request, id):
    service = get_object_or_404(Service, pk=id)
    quantity = int(request.POST.get('quantity'))

    try:
        cartItem = CartItem.objects.get(user=request.user, service=service)
        cartItem.quantity += quantity
    except CartItem.DoesNotExist:
        cartItem = CartItem(
            user=request.user,
            service=service,
            quantity=quantity
        )

    cartItem.save()
    return redirect(reverse('cart'))


def remove_from_cart(request, id):
    CartItem.objects.get(id=id).delete()
    return redirect(reverse('cart'))



