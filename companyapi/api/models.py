from django.db import models

# Create your models here.
# creating company Model

class Company(models.Model):
    company_id = models.AutoField(primary_key =True)
    name = models.CharField( max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices= (('IT','IT'),('Non IT','Non IT'),('Mobiles Phone','Mobile Phone')))
    added_date = models.DateTimeField(auto_now=True)
    active_models = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name  +  self.location
    
    
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('manager','manager'),('software developer','sd'),('project leader','pd')))
    
    
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    
