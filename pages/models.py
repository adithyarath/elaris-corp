from django.db import models
from django.contrib.auth.models import User

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=100)
    type = models.CharField(max_length=15)
 
    def __str__(self):
        return self.user.first_name

class Job(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=200)
    creation_date = models.DateField()
 
    def __str__ (self):
        return self.title

class Application(models.Model):
    company = models.CharField(max_length=200, default="")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume = models.ImageField(upload_to="")
    apply_date = models.DateField()
 
    def __str__ (self):
        return str(self.applicant)