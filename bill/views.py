from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from .models import BillingProfile, Card
from django.utils.http import is_safe_url
from django.conf import settings
# Create your views here.

import stripe
STRIPE_SECRET_KEY = getattr(settings,'STRIPE_SECRET_KEY', 'sk_test_vQMUKe3reph39hVffrrTHINx00hLBGvtxN')
STRIPE_PUB_KEY = getattr(settings,'STRIPE_PUB_KEY' ,'pk_test_YAkn6NLTWIOdoYVdXyh0oyLx0048Jhc6NS')
stripe.api_key = STRIPE_SECRET_KEY

def payment_method_view(request):
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/carts")
    nextUrl = None
    next_ =request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        nextUrl = next_
    return render(request, 'billing/payment-method.html',{"publish_key":STRIPE_PUB_KEY,"nextUrl":nextUrl})

def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            new_card_obj = Card.objects.add_new(billing_profile, token)
        return JsonResponse({"message": "Success! Your card was added."})
    return HttpResponse("error", status_code=401)
    