from django.db import models
from django.contrib.auth.models import User
from qanda.models import Question
from posts.models import Posts
from django.shortcuts import reverse
# Create your models here.

class PostComments(models.Model):
	post=models.ForeignKey(Posts,related_name='posts')
	author=models.ForeignKey(User,related_name='post_comment_author')
	date_created=models.DateField(auto_now=True)
	contents=models.TextField()
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)


	def get_absolute_url(self):
		return reverse('posts:detail',kwargs={'post_pk':self.post.pk})





class QuestionComments(models.Model):
	question=models.ForeignKey(Question,related_name='commented_question')
	author=models.ForeignKey(User,related_name='question_comment_author')
	date_created=models.DateField(auto_now=True)
	contents=models.TextField()
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)



class ReplyPostComments(models.Model):
	comment=models.ForeignKey('PostComments',related_name='reply_post')
	author=models.ForeignKey(User,related_name='reply_author_post')
	date_created=models.DateField(auto_now=True)
	contents=models.TextField()
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)



class ReplyQuestionComments(models.Model):
	comment=models.ForeignKey('QuestionComments',related_name='reply_question')
	author=models.ForeignKey(User,related_name='reply_author_question')
	date_created=models.DateField(auto_now=True)
	contents=models.TextField()
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)



