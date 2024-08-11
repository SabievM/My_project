from django.shortcuts import redirect, render
from cart.models import Cart, CartQueryset
from phone.models import Phone


def user_cart(request):
    carts = Cart.objects.filter(user=request.user)
    return render(request, 'cart/cart.html', {'carts': carts})


def add_cart(request, phone_slug):
    phone = Phone.objects.get(slug=phone_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, phone=phone)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, phone=phone, quantity=1)

    return redirect(request.META['HTTP_REFERER'])



def remove_cart(request, cart_id):
    cart = Cart.objects.filter(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])


