from django import forms
from .models import Comment,User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password',"username","first_name","last_name",]




class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
    
class PaginatorChangePageForm(forms.Form):
    page = forms.IntegerField()