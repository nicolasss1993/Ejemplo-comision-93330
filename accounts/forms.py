from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    # def clean_email(self): # def clean
    #     email = self.cleaned_data["email"]
        
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Ya existe este email")
    #     return email
    
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     breakpoint()
    #     if commit:
    #         self.save()
        
    #     return user



class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ("biografia", "link_web", "avatar")
