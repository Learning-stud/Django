from django.db import models

# Create your models here.


class user(models.Model):
 email = models.EmailField(unique=True,null=False, max_length=50)
 password =models.CharField(max_length=20)
 role = models.CharField( max_length=20)  # chairman/member
 isActive=models.BooleanField(default= False)
 created_at= models.DateTimeField(auto_now= True)
 def __str__(self):
     return self.email+self.password

class Chairman(models.Model):
 userid= models.ForeignKey(user,on_delete=models.CASCADE)
 firstname = models.CharField(max_length = 20)
 lasttname = models.CharField(max_length = 20)
 contact = models.IntegerField(max_length=10)
 blockno= models.CharField(max_length=4)
 houseno=models.CharField(max_length= 4)

 def __str__(self):
        return self.firstname + " | "+self.blockno


class Member(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    blockno = models.CharField(max_length=3)
    houseno = models.CharField(max_length=4)
    occupation = models.CharField(max_length=20)
    job_address = models.TextField()
    bloodgroup = models.CharField(max_length=3)
    vehical_details = models.CharField(max_length=20)
    pic = models.FileField(upload_to="media/upload",default="default.png")
