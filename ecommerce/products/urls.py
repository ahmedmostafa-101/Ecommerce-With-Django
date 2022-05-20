from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('Category/<int:cat_id>/',views.Categories,name="Categories"),
    # path('Product/<int:productid>/',views.Products,name="Products"),
    path('Product/<int:productid>/',views.product_detail,name='product_detail'),
    path('descendingsort/',views.descendingsort,name="descendingsort"),
    path('aescendingsort/',views.aescendingsort,name="aescendingsort"),
    # path('cart/',views.cart,name="cart"),
    path('Product/<int:pid>/cart/',views.add_to_cart,name="add_to_cart"),

]