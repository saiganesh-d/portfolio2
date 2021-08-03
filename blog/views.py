from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render , redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contents import views

from .models import User,Post,Category,Comment,Contact
# Create your views here.
def index(request):
    posts=Post.objects.filter(status="active")
    posts=posts.order_by("-date").all()
    categories=Category.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(posts, 6) # Show 25 contacts per page.
    
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return  render(request,"blog/index.html",{
        
        "categories":categories,
        "users":users
    })
def aboutus(request):
    categories=Category.objects.all()
    return  render(request,"blog/aboutus.html",{
        "categories":categories,
    })

def profile(request,id):
    user=User.objects.get(id=id)
    posts=Post.objects.filter(author_id=id).order_by("-date")
    categories=Category.objects.all()
    return  render(request,"blog/profile.html",{
        "posts":posts,
        "user":user,
        "categories":categories,
        "message":"Profile"
    })

def create_post(request):
    if request.method =="POST":
        author=request.user
        title=request.POST.get("title")
        content=request.POST.get("content")
        image=request.FILES["image"]
        field=request.POST.get("category")
        category=Category.objects.get(name=field)
        post=Post(author=author,title=title,content=content,image=image,field=category)
        post.save()
        return HttpResponseRedirect(reverse("index"))

def category(request,id):
    categories=Category.objects.all()
    posts=Post.objects.filter(field=id)
    posts=posts.order_by("-date").all()
    return  render(request,"blog/profile.html",{
        "posts":posts,
        "categories":categories,
    }) 
@csrf_exempt
@login_required
def toggle_like(request,id):
    if request.method == "PUT":
        post=Post.objects.get(id=id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)  
        post.save()
        return HttpResponse(status=204)
    else:
        return JsonResponse({"error":"PUT request must required"}, status=400) 

@login_required
def liked(request,id):
    user=User.objects.filter(id=request.user.id)
    posts=Post.objects.filter(likes__in=user).order_by("-date")
    categories=Category.objects.all()
    return render(request,"blog/profile.html",{
    "messag":"Liked Articles",
    "posts":posts,
    "categories": categories,
    })

def article(request,id):
    post=Post.objects.get(id=id)
    
    comments=Comment.objects.filter(c_post_id=id)
    categories=Category.objects.all()
    return  render(request,"blog/article.html",{
         "categories":categories,
         "post":post,
         "comments": comments,
    }) 

def contact_view(request):
    categories=Category.objects.all()
    return  render(request,"blog/contact.html",{
         "categories":categories,
}) 

def contact(request):
    if request.method =="POST": 
        user=request.user
        subject=request.POST.get("subject")
        text=request.POST.get("content")
        form=Contact(sender=user,subject=subject,text=text)
        form.save()
        return  render(request,"blog/contact.html",{
         "message":"We have received your message, we will get back to you as soon as possible.",
}) 

def comment(request,id):
    post=Post.objects.get(id=id)
    body=request.POST.get("comment")
    print(body)
    form=Comment(user=request.user,c_post=post,body=body)
    form.save()
    comments=Comment.objects.filter(c_post_id=id)
    categories=Category.objects.all()
    return  render(request,"blog/article.html",{
         "categories":categories,
         "post":post,
         "comments": comments,
    }) 

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "blog/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "blog/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "blog/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "blog/register.html")


def blog_delete(request , id):
    try:
        post=Post.objects.get(id=id)
        if post.author == request.user:
            post.delete()
        
        
        
    except Exception as e :
        print(e)
    author=request.user.id
    user=User.objects.get(id=author)
    posts=Post.objects.filter(author_id=author).order_by("-date")
    categories=Category.objects.all()
    return  render(request,"blog/profile.html",{
        "posts":posts,
        "user":user,
        "categories":categories,
        "message":"Profile"
    })

   