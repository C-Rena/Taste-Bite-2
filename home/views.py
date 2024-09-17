from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User_Recipe,Comment,Contact,Favorite,Rating
from .forms import RecipeForm
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from .models import UserProfile  
from .forms import ProfileImageForm,ProfileUpdateForm
from django.contrib.auth import update_session_auth_hash
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def home_page(request):
    recipes = User_Recipe.objects.all()
    return render(request, "home.html", {"recipes": recipes})


def about_page(request):
    return render(request,"about.html")


@login_required(login_url="account:login")
def recipes_page(request):
    keyword = request.GET.get("keyword", "")
    
    if keyword:
        recipes = User_Recipe.objects.filter(recipe_name__icontains=keyword)
    else:
        recipes = User_Recipe.objects.none()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        
        recipe_list = [
            {
                'id': recipe.id,
                'recipe_name': recipe.recipe_name,
                'image': recipe.image.url if recipe.image else ''  
            }
            for recipe in recipes
        ]
        return JsonResponse({'recipes': recipe_list})
    
    recipes = User_Recipe.objects.all()
    return render(request, "recipes.html", {"recipes": recipes})



@login_required(login_url="account:login")
def my_recipes_page(request):
    recipes = User_Recipe.objects.filter(recipe_owner=request.user)
    return render(request, "my_recipes.html", {"recipes": recipes})


def add_recipe_page(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.recipe_owner = request.user
        recipe.save()
        messages.success(request, "Your recipe has been added with luck...")
        return redirect("my_recipes")

    context = {"form": form}
    return render(request, "add_recipe.html", context)


def recipe_detail_page(request, id):
    recipe=get_object_or_404(User_Recipe,id=id)
    comments=Comment.objects.filter(recipe=recipe)
    context = {
        "recipe": recipe,
        "comments":comments,
        }

    return render(request, "recipe_detail.html", context)


def update_recipe_page(request,id):
    recipe=get_object_or_404(User_Recipe,id=id)
    form=RecipeForm(request.POST or None,request.FILES or None,instance=recipe)
    if form.is_valid():
        recipe=form.save(commit=False)
        recipe.recipe_owner=request.user
        recipe.save()
        messages.success(request,"Your article has been successfully updated...")
        return redirect("my_recipes")

    context={"form":form}
    return render(request,"update.html",context)


def delete_recipe_page(request,id):
    recipe=get_object_or_404(User_Recipe,id=id)
    recipe.delete()
    messages.success(request,"Your recipe has been delete with luck...")
    return redirect("my_recipes")
    


@login_required(login_url="account:login")
def add_comment_page(request,id):
    recipe=get_object_or_404(User_Recipe,id=id)

    if request.method=="POST":
        comment_author=request.POST.get('comment_author')
        comment_content=request.POST.get('comment_content')


        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.recipe=recipe
        newComment.save()
        messages.success(request,"Your comment has been successfully added...")
    return redirect(reverse("recipe_detail",kwargs={"id":id}))




@login_required(login_url="account:login")
def profile_image_update(request):
    
    if not hasattr(request.user, 'userprofile'):
        UserProfile.objects.create(user=request.user)


    if request.method == "POST":
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = ProfileImageForm(instance=request.user.userprofile)

    profile = request.user.userprofile 

 
    context = {
        'form': form,
        'profile': profile,
    }

  
    return render(request, 'profile_image_update.html', context)


@login_required(login_url="account:login")
def delete_profile_image(request):
    profile=request.user.userprofile
    if profile.profile_image.name!='default.png':
        profile.profile_image.delete(save=True)
    profile.profile_image='default.png'
    profile.save()
    return redirect('profile')


@login_required(login_url="account:login")
def contact_page(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")

        contact=Contact(
            name=name,
            email=email,
            message=message,
        )

        contact.save()
        messages.success(request,"Your request has been sent successfully...")

    return render(request,'contact.html')





##########################################################




@login_required(login_url="account:login")
def profile_page(request):
    user = request.user
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            
            
            password = request.POST.get('password')
            if password: 
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user) 

            messages.success(request, "Your profile information has been updated...")
            return redirect('profile')
        else:
            print(profile_form.errors)  

    else:
        profile_form = ProfileUpdateForm(instance=user)

    context = {
        'profile_form': profile_form,
        'user': user,
    }
    return render(request, 'profile.html', context)

#######################################################################3
@login_required(login_url="account:login")
def catageory_page(request):
    return render(request,"catageory.html")

##########################################################################


def recipes_by_category(request, category_name):
    recipes = User_Recipe.objects.filter(category=category_name) 
    context = {
        'recipes': recipes,
        'category_name': category_name,
    }
    return render(request, 'recipes_by_category.html', context)



######################################################

def rate_recipe(request,recipe_id):
    recipe=get_object_or_404(User_Recipe,id=recipe_id)
    if request.method=="POST":
        rating_value=request.POST.get('rating')
        if rating_value:
            rating, created=Rating.objects.get_or_create(user=request.user,recipe=recipe)
            rating.rating=rating_value
            rating.save()
            messages.success(request,"Your rating has been submitted...")

        else:
            messages.error(request,"Please select a rating before sumbitting...")
    
    return redirect('recipe_detail',id=recipe_id)


################################################################

def add_to_favorites(request,recipe_id):
    recipe=get_object_or_404(User_Recipe,id=recipe_id)
    favorite,created=Favorite.objects.get_or_create(user=request.user,recipe=recipe)

    if created:
        messages.success(request,"Recipe added to favorites....")

    else:
        messages.warning(request,"This recipe is already in your favorites....")

    return redirect("recipe_detail",id=recipe_id)


def favorite_recipes(request):
    favorites=Favorite.objects.filter(user=request.user)
    return render(request,'favorite_recipes.html',{'favorites':favorites})





###############################################



def add_to_favorites(request, recipe_id):
    recipe = get_object_or_404(User_Recipe, id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)

    if created:
        messages.success(request, "Recipe added to favorites....")
    else:
        messages.warning(request, "This recipe is already in your favorites....")

    return redirect("recipe_detail", id=recipe_id)

def favorite_recipes(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorite_recipes.html', {'favorites': favorites})

def select_favorites(request):
  
    messages.info(request, "Selected items.")
    return redirect('favorite_recipes')

def select_all_favorites(request):

    messages.info(request, "All items selected.")
    return redirect('favorite_recipes')
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Favorite

def delete_selected_favorites(request):
    if request.method == "POST" and 'delete' in request.POST:
        selected_favorites = request.POST.getlist('selected_favorites')
        if selected_favorites:
          
            Favorite.objects.filter(id__in=selected_favorites, user=request.user).delete()
            messages.success(request, "Deleted selected favorite recipes...")
        else:
            messages.warning(request, "You have not selected any recipe to delete...")
    return redirect('favorite_recipes')


##############################################################


# from django.http import HttpResponse
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter

def download_recipe_pdf(request, id):
    
    recipe = get_object_or_404(User_Recipe, id=id)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{recipe.recipe_name}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter  

    p.drawString(50, height - 50, f"Recipe Name: {recipe.recipe_name}")
    p.drawString(50, height - 80, f"Recipe Details: {recipe.recipe}")

    
    p.showPage()
    p.save()
    
    return response


###############################################
# from django.http import HttpResponse
# from reportlab.pdfgen import canvas


def download_recipe_pdf(request, id):
   
    recipe = get_object_or_404(User_Recipe, id=id)
    
 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{recipe.recipe_name}.pdf"'

   
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter  
    
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 50, f"Recipe Name: {recipe.recipe_name}")
    p.drawString(50, height - 70, f"Recipe Details: {recipe.recipe}")

    text = p.beginText(50, height - 90)
    text.setFont("Helvetica", 12)
    text.setTextOrigin(50, height - 90)
   
    text.textLines([
        f"Recipe Name: {recipe.recipe_name}",
        f"Recipe Details: {recipe.recipe}"
    ])

    p.drawText(text)


    p.showPage()
    p.save()
    
    return response
