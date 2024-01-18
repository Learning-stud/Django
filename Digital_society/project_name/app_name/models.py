from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    isActive = models.BooleanField(default=False)
    createdat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} | {self.password}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    blockno = models.CharField(max_length=4)
    houseno = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.first_name} | {self.block_no}"

class Chairman(Profile):
    pass

class Member(Profile):
    occupation = models.CharField(max_length=20)
    jobaddress = models.TextField()
    bloodgroup = models.CharField(max_length=3)
    vehicledetails = models.CharField(max_length=20)
    pic = models.FileField(upload_to="media/upload", default="default.png")

    def __str__(self):
        return f"{self.first_name} | {self.block_no}"