from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField


class User_Recipe(models.Model):
    recipe_owner= models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name=models.CharField(max_length=50)
    recipe = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image=models.FileField(upload_to="Recipe imgs",blank=True,null=True)

    def __str__(self):
        return self.recipe_owner.username

