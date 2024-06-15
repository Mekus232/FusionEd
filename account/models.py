from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


STATUS_CHOICE = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejected", "Rejected")
)

class Grade(models.Model):
    grade = models.IntegerField()
    
    
    class Meta:
        ordering = ["grade"]
    
    def __str__(self):
        return f"Grade {str(self.grade)}"
class User(AbstractUser):
    def __str__(self):
        return self.first_name + " " + self.last_name
    


class Teacher(User):
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    image = models.FileField(upload_to="photo",blank=True, verbose_name="Photo",)
    status = models.CharField(max_length=50, null=True, choices=STATUS_CHOICE, default="Pending")
    class Meta:
        pass
        # proxy = True
        # ordering = ['-date_joined']
        
class Student(User):
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)
    birth = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Birthday")
    gender = models.CharField(max_length=10)
    image = models.FileField(upload_to="photo", verbose_name="Photo",)
    status = models.CharField(max_length=50, null=True, choices=STATUS_CHOICE, default="Pending")
    request_password = models.BooleanField(null=False, default=False)
    

