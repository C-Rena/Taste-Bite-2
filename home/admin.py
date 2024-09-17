from django.contrib import admin
from .models import User_Recipe, Comment,Contact


admin.site.register(Contact)

@admin.register(User_Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["recipe_name", "recipe_owner"]
    list_display_links = ["recipe_name", "recipe_owner"]
    list_filter = ["time"]
    search_fields = ["recipe_name"]

    class Meta:
        model = User_Recipe

@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment_author"]
    list_display_links = ["comment_author"]
    list_filter = ["comment_date"]
    search_fields = ["comment_author"]

    class Meta:
        model = Comment
