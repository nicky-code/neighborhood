from django.shortcuts import render
from django.http  import HttpResponse
from .models import Neighborhood,Profile,Business

# Create your views here.
def welcome(request):
    
    current_user = request.user
    neighbours = Neighborhood.objects.all()
    profile = Profile.objects.filter(user=current_user).first()
    return render(request, 'welcome.html',{'neighbours':neighbours,'profile':profile})


def neighborhood(request,neighborhood_id):
    
    current_user = request.user
    neighbours = Neighborhood.objects.get(id=neighborhood_id)
    print(neighbours)
    
    profile=Profile.objects.filter(id=current_user.id).first()
    businesses=Business.objects.filter(id=neighbours.id).all()
    return render(request, 'neighborhood.html',{'businesses':businesses,'neighbours':neighbours,'neighborhood_id':neighborhood_id})


