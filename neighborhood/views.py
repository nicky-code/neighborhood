from django.shortcuts import render
from django.http  import HttpResponse
from .models import Neighborhood,Profile,Business
from .forms import ProfileForm,BusinessForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    
    current_user = request.user
    neighbours = Neighborhood.objects.all()
    profile = Profile.objects.filter(user=current_user).first()
    return render(request, 'welcome.html',{'neighbours':neighbours,'profile':profile})



@login_required(login_url='/accounts/login/')
def neighborhood(request,neighborhood_id):
    
    current_user = request.user
    neighbours = Neighborhood.objects.get(id=neighborhood_id)
    print(neighbours)
    
    profile=Profile.objects.filter(id=current_user.id).first()
    businesses=Business.objects.filter(id=neighbours.id).all()
    return render(request,'neighborhood.html',{'businesses':businesses,'neighbours':neighbours,'neighborhood_id':neighborhood_id})


@login_required(login_url='/accounts/login/')
def new_profile(request):
    
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance =profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('myProfile')

    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'new-profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def myProfile(request):
    
   current_user = request.user 
   profile = Profile.objects.filter(user = current_user).first()
   return render(request, 'profile.html', {"profile":profile})


@login_required(login_url='/accounts/login/')
def new_business(request):

    current_user = request.user
    if request.method == 'POST':

        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business_post = form.save(commit=False)
            business_post.user = current_user
            business_post.save()
            return redirect('profile')
       

    else:
        form = BusinessForm()
        return render(request,'business.html', {"form": form})


