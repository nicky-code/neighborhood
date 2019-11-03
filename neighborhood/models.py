from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(max_length=30)
    occupantsCount = models.CharField(max_length=30)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.neighbourhood_name
    
    @classmethod
    def create_neighborhood(self):
        self.save()
        
    
    def delete_neigborhood(self):
        self.delete()
        
    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        area = cls.objects.filter(id=neigborhood_id)
        return area
    
    def update_neighborhood():
        self.update()
        
        
    def  update_occupantsCount():
        occupantsCount = self.update_occupantsCount.update()
        self.occupantsCount
        
       
class Profile(models.Model):
    firstName= models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    neighborhood = models.ForeignKey(Neighborhood)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.profile
        
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    def update_profile(self):
        self.update()
        
        
class Business(models.Model):
    business_name = models.CharField(max_length=40)
    business_email = models.CharField(max_length=40)
    neighborhood = models.ForeignKey(Neighborhood)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.business
    
    
    def create_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
        
    @classmethod
    def find_business(cls,business_id):
        businesses = cls.objects.filter(id=business_id)
        return businesses
    
    def update_business(self):
        self.update()
        