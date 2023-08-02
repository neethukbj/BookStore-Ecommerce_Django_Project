"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.HOME,name='index'),


    path('',views.COLLECTIONS,name='collections'),
    path('fiction/',views.FICTION,name='fiction'),
    path('biographies/',views.BIOGRAPHIES,name='biographies'),
    path('childrens/',views.CHILDRENS,name='childrens'),
    path('thriller/',views.THRILLER,name='thriller'),
    path('classics/',views.CLASSICS,name='classics'),
    path('selfhelp/',views.SELFHELP,name='selfhelp'),
    path('allbooks/',views.ALLBOOKS,name='allbooks'),
    path('about/',views.ABOUT,name='about'),
    path('blog/',views.BLOG,name='blog'),
    path('new/',views.NEW,name='new'),


    path('allbooks/book_details/<str:id>',views.BOOK_DETAILS,name='book_details'),
    path('allbooks/quick_view/<str:id>',views.QUICK_VIEW,name='quick_view'),
    path('contact/',views.CONTACT_PAGE,name='contact'),
    path('signup/',views.HANDLESIGNUP,name='signup'),
    path('login/',views.HANDLELOGIN,name='login'),
    path('logout/',views.HANDLELOGOUT,name='logout'),
    path('auth/',views.AUTH,name='auth'),


#cart 
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('cart/checkout/',views.CHECK_OUT,name='checkout'),
    path('cart/review/',views.REVIEW,name='review'),
    path('cart/checkout/placeorder',views.PLACE_ORDER,name='place_order'),
    path('success',views.SUCCESS,name='success'),

    path('Your_Order',views.YOUR_ORDER,name='your_order'),

    path('add-to-cart',views.ADDTOCART,name='addtocart'),

   











    







    path('base/',views.BASE,name='base'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

#,