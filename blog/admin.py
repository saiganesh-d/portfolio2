from django.contrib import admin
from .models import User,Post,Category,Comment,Contact

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=[
        "username"
    ]
class PostAdmin(admin.ModelAdmin):
    list_display=[
        "author",
        "title",
        
        "status",
    ]
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        "name"
    ]
class CommentAdmin(admin.ModelAdmin):
    list_display=[
        "user",
        "c_post"
    ]
class ContactAdmin(admin.ModelAdmin):
    list_display=[
        "sender",
        "subject"
    ]

admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Category,CategoryAdmin)