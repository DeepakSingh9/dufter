from django.shortcuts import render
from .models import Post

# Create your views here.
def Post_List(request):
    return render(request,'blog/index.html',{})
