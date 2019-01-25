from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect,reverse
from groups.models import Groups



class Question(models.Model):
	author=models.ForeignKey(User, related_name='question_author')
	que=models.TextField()
	date_created=models.DateField(auto_now=True)
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)
	group=models.ForeignKey(Groups, related_name='question_group')


	def __str__(self):
		return self.que

	def get_absolute_url(self):
		return reverse('qanda:detail' ,kwargs={'que_pk':self.pk})



class Answer(models.Model):
	author=models.ForeignKey(User, related_name='answer_author')
	ans=models.TextField()
	date_created=models.DateField(auto_now=True)
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)
	que=models.ForeignKey('Question', related_name='question')


	def __str__(self):
		return self.ans

	def get_absolute_url(self):
		return reverse('qanda:detail',kwargs={'que_pk':self.que.pk})
