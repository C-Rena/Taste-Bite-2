from django import forms
from .models import User_Recipe,UserProfile
from django.contrib.auth.models import User

class RecipeForm(forms.ModelForm):
    class Meta:
        model = User_Recipe
        fields = ["recipe_name", "recipe", "image", "category"]  # category alanını ekledik


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['profile_image']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Sadece username ve email alanları
