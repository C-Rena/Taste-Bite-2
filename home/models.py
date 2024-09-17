from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField



class User_Recipe(models.Model):
    CATEGORIES=[
        ('Seefood','Seefood'),
        ('Soup','Soup'),
        ('Pancakes','Pancakes'),
        ('Meat','Meat'),
        ('Chicken','Chicken'),
        ('Less than 30 min','Less than 30 min'),
        ('Pasta','Pasta'),
        ('Pizza','Pizza'),
        ('Cake','Cake'),
        ('Pastries', 'Pastries'),
        ('Burger', 'Burger'),
        ('Vegan', 'Vegan'),
        ('Desserts', 'Desserts'),
        ('Smoothies', 'Smoothies'),
        ('Breakfast', 'Breakfast'),
        ('Salad', 'Salad'),
        ('Sandwiches', 'Sandwiches'),
        ('Waffles', 'Waffles'),
        ('Ramen', 'Ramen'),
        ('Dips', 'Dips'),
    ]
    recipe_owner= models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name=models.CharField(max_length=50)
    recipe = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="Recipe imgs")  
    category=models.CharField(max_length=50,choices=CATEGORIES,default='Seefood')

    def __str__(self):
        return f"{self.recipe_name} | {self.recipe_owner}"


class Comment(models.Model):
    recipe=models.ForeignKey(User_Recipe,on_delete=models.CASCADE, verbose_name="Resept",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="Ad")
    comment_content=models.TextField(verbose_name="serh")
    comment_date= models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.comment_author}"



class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.FileField(upload_to='profile_images/',default='default.png')

    def __str__(self):
           return f'{self.user.username} UserProfile'
    


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.TextField(max_length=200)

    def __str__(self):
        return self.name


########################################

class Rating (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recipe=models.ForeignKey(User_Recipe,on_delete=models.CASCADE)
    rating=models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} rated {self.recipe.recipe_name} as {self.rating} stars"
    

#######################################

class Favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recipe=models.ForeignKey(User_Recipe,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} favorited {self.recipe.recipe_name}"