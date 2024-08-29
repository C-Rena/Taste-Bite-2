from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_page,name="home"),
    path("about/",about_page,name="about"),
    path("profile/",profile_page,name="profile"),
    path("recipes/",recipes_page,name="recipes"),
    path("my_recipes/",my_recipes_page,name="my_recipes"),
    path("add_recipe/",add_recipe_page,name="add_recipe"),
    path("recipe_detail/<int:id>",recipe_detail_page,name="recipe_detail"),
    path("update/<int:id>",update_recipe_page,name="update"),
    path("delete/<int:id>",delete_recipe_page,name="delete"),
    path("account/",include("account.urls")),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)