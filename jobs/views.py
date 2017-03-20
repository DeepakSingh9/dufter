from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from .forms import UserRegistrationForm
from django.views.generic import View


# Create your views here.
from .models import JobCategory,Job,Profile
from .forms import UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required


def Job_Category_List(request):
    category_list=JobCategory.objects.all()
    job=Job.objects.all()
    return render(request,'index.html',{'category_list':category_list,'job':job})




def user_registration(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            profile=Profile.objects.create(user=new_user)
            new_user.save()
            return render(request,'jobs/registeration.html',{'new_user':new_user})
    else:
        user_form=UserRegistrationForm
    return render(request,'jobs/registeration.html',{'user_form':user_form})




@login_required
def edit(request):
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,
                               data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,
                                     data=request.POST,
                                     files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request,'jobs/accountedit.html',{'user_form':user_form,'profile_form':profile_form})