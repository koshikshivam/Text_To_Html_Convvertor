from django.shortcuts import render
from .models import Post
from   Text_Project_App.forms import PostForm

def home(request):
    form=PostForm()
    return render(request,'blog/home.html',{'form':form})


