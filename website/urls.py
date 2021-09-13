from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('index.html', views.index, name="index"),
	path('product.html', views.product, name="product"),
	path('blog.html', views.blog, name="blog"),
	path('about.html', views.about, name="about"),
	path('contact.html', views.contact, name="contact"),
	path('blog-detail.html', views.blogdetail, name="blogdetail"),
	path('product-detail.html', views.productdetail, name="productdetail"),
	path('login.html', views.login, name="login"),
	path('register.html', views.register, name="register"),
	path('store.html', views.store, name="store"),
	path('cart.html', views.cart, name="cart"),
	path('checkout.html', views.checkout, name="checkout"),
	path('home03.html', views.home03, name="home03"),
	
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]



