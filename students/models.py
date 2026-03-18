from django.db import models

# Student Model
class student(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    college = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    jdate = models.CharField(max_length=30, null=True)
    totalf = models.CharField(max_length=30, null=True)
    paidf = models.CharField(max_length=30, null=True)
    leftf = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)
    technology = models.CharField(max_length=30, null=True)
    image = models.FileField(upload_to='students/', null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name