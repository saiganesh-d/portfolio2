from django import forms

from .models import Post,Comment,Contact

class PostForm (forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","content", "image", "field",]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=[ "body","c_post"]

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["subject","text"]