from django.db import models

# Create your models here.


class usere(models.Model):
 email = models.EmailField(unique=True, max_length=50)
 password =models.CharField(max_length=20)
 role = models.CharField( max_length=20)  # chairman/member 