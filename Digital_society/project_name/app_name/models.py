from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} | {self.password}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    block_no = models.CharField(max_length=4)
    house_no = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.first_name} | {self.block_no}"

class Chairman(Profile):
    pass

class Member(Profile):
    occupation = models.CharField(max_length=20)
    job_address = models.TextField()
    blood_group = models.CharField(max_length=3)
    vehicle_details = models.CharField(max_length=20)
    pic = models.FileField(upload_to="media/upload", default="default.png")

    def __str__(self):
        return f"{self.first_name} | {self.block_no}"