"""order_food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.validation,name='validation'),
    path('check',views.check,name='checks'),
    path('signup/',views.signup,name='signup'),
    path('emailverfication',views.sent_otp,name='sent_otp'),
    path('verify' , views.verify),                                                                                            
    path('cart/' , views.cart , name='cart'),
    path('profile/' , views.profile , name='Profile'),
    path('add1' , views.add1 , name='add1'),
    path('add2',views.add2,name='add2'),
    path('add3',views.add3,name='add3'),
    path('add4' , views.add4 , name='add4'),
    path('add5' , views.add5 , name='add5'),
    path('add6' , views.add6 , name='add6'),
    path('add7' , views.add7 , name='add7'),
    path('add8' , views.add8 , name='add8'),
    path('add9' , views.add9 , name='add9'),
    path('add10' , views.add10 , name='add10'),
    path('add11' , views.add11 , name='add11'),
    path('add12' , views.add12 , name='add12'),
    path('add13' , views.add13 , name='add13'),
    path('add14' , views.add14 , name='add14'),
    path('add15' , views.add15 , name='add15'),
    path('add16' , views.add16 , name='add16'),
    path('add17' , views.add17 , name='add17'),
    path('add18' , views.add18 , name='add18'),
    path('add19' , views.add19 , name='add19'),
    path('add20' , views.add20 , name='add20'),
    path('cart/order' , views.order , name='order'),
    path('profile/order_history' , views.order_history , name='history'),    
    path('foods/' , views.foods , name='foods'),
    path('profile/change_address' , views.address, name='changing address'),
    path('profile/changing' , views.changing , name='changing address')
]
