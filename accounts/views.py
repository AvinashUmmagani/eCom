from django.shortcuts import render, redirect
from .forms import loginForm, registerForm, GuestForm
from .models import GuestMail
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView
from .signals import user_logged_in

# Create your views here.
def guest_register_page(request):
    form = GuestForm(request.POST or None)
    context = {"form":form}
    next_ =request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():  
        email = form.cleaned_data.get('e_mail')
        new_guest_email = GuestMail.objects.create(email = email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/carts/checkout")    
    return render(request,"/accounts/register/",context)

class LoginView(FormView):
    form_class = loginForm
    template_name = "accounts/login.html"
    success_url = "/"
    def form_valid(self, form):
        request = self.request
        next_ =request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')    
        user = authenticate(request, username = email, password = password)
        if user is not None:
            login(request, user)
            user_logged_in.send(user.__class__, instance=user,request= request)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('home')
        return super(LoginView, self).form_invalid()





class RegisterView(CreateView):
    form_class = registerForm
    template_name = "accounts/register.html"
    success_url = "/accounts/login/"





# def login_page(request):
#     form = loginForm(request.POST or None)
#     context = {"form":form}
#     print("User Logged in")
#     print(request.user.is_authenticated)
#     next_ =request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     if form.is_valid():  
#         username = form.cleaned_data.get('userName')
#         password = form.cleaned_data.get('password')    
#         user = authenticate(request = request, username = username, password = password)

#         if user is not None:
#             login(request, user)
#             try:
#                 del request.session['guest_email_id']
#             except:
#                 pass
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect('home')   
#         else:
#             print("Error")
#     return render(request,"accounts/login.html",context)
