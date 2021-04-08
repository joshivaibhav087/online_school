from django.db import models
from account.models import User
from django.shortcuts import reverse
from embed_video.fields import EmbedVideoField
# Create your models here.
class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class1 = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    chapter = models.CharField(max_length=20)
    video = EmbedVideoField()
    notes = models.TextField()
    approved =models.BooleanField(default=False)

    def __str__ (self):
        return str(self.subject)