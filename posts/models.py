from django.db import models
from django.contrib.auth.models import User
from groups.models import Groups 
from django.shortcuts import reverse

# Create your models here.


class Posts(models.Model):
	title=models.CharField(max_length=200)
	tag=models.CharField(max_length=100)
	content=models.TextField()
	date_created=models.DateField(auto_now=True)
	date_published=models.DateField(default=None,null=True)
	author=models.ForeignKey(User,related_name='post_author')
	group=models.ForeignKey(Groups,related_name='post_group',null=True)
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)
	liked_by=models.ManyToManyField(User,related_name='like_user')
	disliked_by=models.ManyToManyField(User,related_name='dislike_user')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('groups:detail',kwargs={'pk':self.group.pk})

