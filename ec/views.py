from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import contactForm
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    contact_form = contactForm(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message":"Thanks for your submission"})
    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors,status = 400, content_type = 'application/json')
    return render(request,'contact.html',{'form':contact_form})

