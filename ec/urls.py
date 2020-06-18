"""ec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from address import views as ad_views
from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url
from bill.views import payment_method_view, payment_method_createview
from carts.views import cart_detail_api_view 
from marketing.views import MarketingPreferenceUpdateView, MailchimpWebhookView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^checkout/address/use$',ad_views.checkout_address_use_view,name='checkout_address_use'),
    url(r'^checkout/address/create$',ad_views.checkout_address_create_view,name='checkout_address_create'),
    url(r'^product/',include(('product.urls','product'), namespace='product')),
    url(r'^accounts/',include(('accounts.urls','accounts'), namespace='accounts')),
    url(r'^search/',include(('search.urls','search'), namespace='search')),
    url(r'^carts/',include(('carts.urls','carts'), namespace='carts')),
    url(r'api/cart/',cart_detail_api_view,name = 'api-cart'),
    url(r'billing/payment-method/$',payment_method_view,name = 'billing-payment-method'),
    url(r'billing/payment-method/create/$',payment_method_createview,name = 'billing-payment-method-endpoint'),
    url(r'^settings/email/$', MarketingPreferenceUpdateView.as_view(), name = 'marketing-pref'),
    url(r'^webhooks/mailchimp/$', MailchimpWebhookView.as_view(), name = 'webhooks-mailchimp'),
]   

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)