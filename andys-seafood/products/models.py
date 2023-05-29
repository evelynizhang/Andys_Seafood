from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.email_address
