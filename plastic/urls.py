"""plastic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views 
from django.conf import settings
from django.conf.urls.static import static

from plasticapp.views import FactoryReg, IndexView, PanchayathReg, UserReg, login_view,payment,paymentch,bill,ch
from plasticapp import views
from plasticapp import admin_urls, factory_urls, panchayath_urls, user_urls




urlpatterns = [
    path('', IndexView.as_view()),
    path('logout_user',views.logout_user,name='logout_user'),
    path('user_reg', UserReg.as_view()),
    path('p_reg', PanchayathReg.as_view()),
    path('f_reg', FactoryReg.as_view()),
    path('login', login_view.as_view(),name='login'),
    path('admin/',admin_urls.urls()),
    path('panchayath/',panchayath_urls.urls()),
    path('user/',user_urls.urls()),
    path('factory/',factory_urls.urls()),
    path('payment',payment.as_view(),name="payment"),
    path('paymentch',paymentch.as_view(),name="paymentch"),
    path('bill',bill.as_view(),name='bill'),
    path('ch',ch.as_view(),name='ch'),


]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

