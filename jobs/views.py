from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate

# Create your views here.
from .models import JobCategory,Job
from .forms import LoginForm

def Job_Category_List(request):
    category_list=JobCategory.objects.all()
    job=Job.objects.all()
    return render(request,'index.html',{'category_list':category_list,'job':job})


def user_login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],
                              password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request ,user)
                    return HttpResponse('AUTHENTICATED SUCCESSFULLY')
                else:
                    return HttpResponse('Account Disabled')
            else:
                return HttpResponse('Invalid login')
        else:
            form=LoginForm()

        return render(request,'jobs/login_form.html',{'form':form})
