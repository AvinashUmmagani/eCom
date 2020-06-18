from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','full_name', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]






class GuestForm(forms.Form):
    e_mail = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"E-mail",
                "name":"contact_email",
           }
       )
    )
    def clean_e_mail(self):
        email = self.cleaned_data.get('e_mail')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already taken")
        return email



class loginForm(forms.Form):
    email = forms.EmailField(label='Email',
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Email",
                "name":"email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Password",
                "name":"Userpassword",
            }
        )
    )


class registerForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
                "class":"form-control",
                "placeholder":"Password",
                "name":"Userpassword",
            }
    ))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(
        attrs={
                "class":"form-control",
                "placeholder":"Confirm Password",
                "name":"conifirmPassword",
            }
    ))

    class Meta:
        model = User
        fields = ('email', 'full_name')
        widgets={ 
            'email': forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Email",
                "name":"email",
            }),
            'full_name': forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"User Name",
                "name":"userName",
            })
            
        }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(registerForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        #user.active = False
        if commit:
            user.save()
        return user





# class registerForm(forms.Form):
#     userName = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class":"form-control",
#                 "placeholder":"User Name",
#                 "name":"userName",
#             }
#         )
#     )
#     e_mail = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class":"form-control",
#                 "placeholder":"E-mail",
#                 "name":"contact_email",
#            }
#        )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             
#         )
#     )
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class":"form-control",
#                 "placeholder":"Confirm Password",
#                 "name":"conifirmPassword",
#             }
#         )
#     )
#     def clean_confirm_password(self):
#         p=self.cleaned_data.get('password')
#         cp=self.cleaned_data.get('confirm_password')
#         if p != cp:
#             raise forms.ValidationError("Password mismatch")
#         return cp

#     def clean_userName(self):
#         username = self.cleaned_data.get('userName')
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError("Username already taken")
#         return username
    
#     def clean_e_mail(self):
#         email = self.cleaned_data.get('e_mail')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email already taken")
#         return email
