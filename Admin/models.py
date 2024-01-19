from django.db import models
# from Employee.models import EMPLOYEE////////

# Create your models here.
class ADMIN(models.Model):
    id = models.IntegerField(primary_key=True,auto_created = True)
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()

class COMPANY(models.Model):
    id = models.IntegerField(primary_key = True,auto_created = True)
    name = models.TextField(unique = True)
    logo = models.ImageField(upload_to="company_logo/",null= True)

