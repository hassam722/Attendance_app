from django.db import models
from Admin.models import COMPANY

# Create your models here.
class EMPLOYEE(models.Model):
    id = models.IntegerField(primary_key= True,auto_created =True)
    name = models.TextField()
    email= models.TextField(unique = True)
    password = models.TextField()
    role = models.TextField()
    gender = models.TextField(null =True)
    access = models.TextField()
    salary = models.PositiveIntegerField()
    deduction = models.IntegerField()
    com_id = models.ForeignKey(COMPANY,on_delete =models.CASCADE)
    image = models.ImageField(upload_to="emp_images/",null= True)
    

class ATTENDANCE_REGISTER(models.Model):
    id = models.IntegerField(primary_key =True,auto_created = True)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(null= True)
    Time_diff = models.TimeField(null= True)
    Emp_id = models.ForeignKey(EMPLOYEE,on_delete = models.CASCADE)