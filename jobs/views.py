from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.views.generic import View



# Create your views here.
from .models import JobCategory,Job,Profile
from django.contrib.auth.decorators import login_required
from .forms import UserForm,UserProfileForm



def home_view(request):
    category_list = JobCategory.objects.all()
    job = Job.objects.all()[:5]
    return render(request, 'jobs/index.html', {'category_list': category_list, 'job': job})




def Category_Job_List(request,pk):
    category=JobCategory.objects.get(pk=pk)
    job=Job.objects.all()
    return render(request,'jobs/category_job_list.html',{'category':category,'job':job})




def registration(request):
    registered=False


    if request.method=='POST':
        user_form=UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True

        else:
            print user_form.errors,profile_form.errors



    else:
        profile_form=UserProfileForm()
        user_form=UserForm()

    return render(request,'jobs/registeration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})






def User_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)


        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/jobs/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print 'invalid login details :{0},{1}'.format(username,password)
            return HttpResponse("invalid login details")



    return render(request,'jobs/login.html',{})


@login_required()
def User_Logout(request):
    logout(request)

    return HttpResponseRedirect('/jobs/')