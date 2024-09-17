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
    path("my_recipes/",my_recipes_page,name='my_recipes'),
    path("add_recipe/",add_recipe_page,name="add_recipe"),
    path("recipe_detail/<int:id>",recipe_detail_page,name="recipe_detail"),
    path("update/<int:id>",update_recipe_page,name="update"),
    path("delete/<int:id>",delete_recipe_page,name="delete"),
    path("comment/<int:id>",add_comment_page,name="comment"),
    path('profile/image/update',profile_image_update,name='profile_image_update'),
    path('profile/image/delete/', delete_profile_image, name="profile_image_delete"),
    path('categories/',catageory_page,name="catageory"),
    path('contact/',contact_page,name='contact'),
    path('recipes/<str:category_name>/', recipes_by_category, name='recipes_by_category'),
    path('rate-recipe/<int:recipe_id>/', rate_recipe, name='rate_recipe'),
    path('add-to-favorites/<int:recipe_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/', favorite_recipes, name='favorite_recipes'),
    path('add_to_favorites/<int:recipe_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorite_recipes/', favorite_recipes, name='favorite_recipes'),
    path('select_favorites/', select_favorites, name='select_favorites'),
    path('select_all_favorites/', select_all_favorites, name='select_all_favorites'),
    path('delete_selected_favorites/', delete_selected_favorites, name='delete_selected_favorites'),

    path('recipe/<int:id>/', recipe_detail_page, name='recipe_detail'),
    path('recipe/<int:id>/download/', download_recipe_pdf, name='download_recipe_pdf'),
    path("account/",include("account.urls")),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)