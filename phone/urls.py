from phone import views
from django.urls import path

app_name='phone'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('<slug:slug>/', views.index, name='index'),
    path('phone-detail/<slug:phone_slug>/', views.phone_detail, name='phone-detail'),
    #path('filter/<slug:color>/', views.index, name='color'), Этот путь работает для закомментрированного фильтра в шаблоне index приложения phone
]
