from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect,reverse

# Create your models here.


class Groups(models.Model):
	name=models.CharField(max_length=200)
	tag=models.CharField(max_length=50)
	description=models.TextField()
	admin=models.ForeignKey(User,on_delete=models.CASCADE,related_name='groupadmin')
	pic=models.ImageField(upload_to="group_pic")
	members=models.ManyToManyField(User,related_name='groupmembers')
	hidden=models.BooleanField(default=False)
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('groups:join',kwargs={'pk':self.pk})


