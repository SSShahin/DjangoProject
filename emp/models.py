from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    is_working=models.BooleanField(default=True)
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to='testimonial/')
    rating=models.IntegerField()

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    email=models.EmailField(max_length=254)
    name=models.CharField(max_length=50)
    feedback=models.CharField(max_length=100)

    def __str__(self):
        return self.name