from cart import views
from django.urls import path


app_name='phone'

urlpatterns = [
    path('user/', views.user_cart, name='user_cart'),
    path('add-cart/<slug:phone_slug>', views.add_cart, name='add-cart'),
    path('delete/<int:cart_id>', views.remove_cart, name='delete')
]