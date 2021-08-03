from os import name
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("", views.index, name="index"),
    path("register",views.register, name="register"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("profile/<int:id>",views.profile, name="profile"),
    path("aboutus",views.aboutus, name="aboutus"),
    path("create_post",views.create_post, name="create_post"),
    path("category/<int:id>",views.category, name="category"),
    path("contact_view",views.contact_view, name="contact_view"),
    path("contact",views.contact, name="contact"),
    path("liked/<int:id>",views.liked, name="liked"),
    path("article/<int:id>",views.article, name="article"),
    path("comment/<int:id>",views.comment, name="comment"),
    path('blog-delete/<id>' , views.blog_delete , name="blog_delete"),
    
    #API routes
    path("toggle_like/<int:id>",views.toggle_like, name="toggle_like"),
    path("profile/toggle_like/<int:id>",views.toggle_like, name="profile/toggle_like"),
    path("liked/toggle_like/<int:id>",views.toggle_like, name="liked/toggle_like"),
    path("article/toggle_like/<int:id>",views.toggle_like, name="article/toggle_like"),
]
