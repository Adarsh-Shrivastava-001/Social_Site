from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	city=models.CharField(max_length=100)
	signed=models.BooleanField(default=False)
	birthday=models.DateField()
	pic=models.ImageField(upload_to="profile_pics",blank=True)

	def __str__(self):
		return self.user.username
