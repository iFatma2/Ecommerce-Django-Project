from django.contrib import admin
from django.urls import path
from flower import views
from flower import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),


    path('productdetails/<int:id>/', views.productdetails, name='productdetails'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shipping_address/', views.shipping_address, name='shipping_address'),
    path('payment/', views.payment, name='payment'),

    path('auth_login/', views.auth_login, name='auth_login'),
    path('auth_register/', views.auth_register, name='auth_register'),
    path('auth_logout/', views.auth_logout, name='auth_logout'),


    # path('api/itemlist/all', v1.getAllItems, name='getAllItems'),
    # path('api/get_item_details/all', v1.get_item_details, name='get_item_details'),
    # path('api/get_item_details_byid/all/<int:id>/', v1.get_item_details_byid, name='get_item_details_byid'),
]
