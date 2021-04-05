from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    age = models.IntegerField()
    id_proof = models.ImageField(upload_to="idprof")
    gender = models.CharField(max_length=20)
    class1 = models.CharField(max_length=20)
    approve = models.BooleanField(default=False)
        
    def __str__(self):
        return str(self.user)