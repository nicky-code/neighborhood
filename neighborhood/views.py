from django.shortcuts import render
from django.http  import HttpResponse
from .models import Neighborhood,Profile,Business

# Create your views here.
def welcome(request):
    
    current_user=request.current_user
    neighbours = Neighborhood.objects.all()
    profile = Profile.objects.filter(user=current_user).first()
    return render(request, 'welcome.html',{'neighbours':neighbours,'profile':profile})