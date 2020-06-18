from django import forms
from django.contrib.auth.models import User

class contactForm(forms.Form):
    full_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Full Name",
                "name":"fullname"
            }
        )
    )
    e_mail = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"E-mail",
                "name":"contact_email",
                }
            )
        )
    context = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"context",
                "name":"contact_context",
                }
            )
        )
    # def clean_e_mail(self):
    #     email = self.cleaned_data.get("e_mail")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email should end with @gmail.com")
    #     return email
    
    
