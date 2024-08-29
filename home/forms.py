from django import forms
from .models import User_Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model=User_Recipe
        fields=["recipe_name","recipe","image"]
