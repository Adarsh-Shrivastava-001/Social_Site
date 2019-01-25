from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView
from .models import PostComments,QuestionComments,ReplyPostComments,ReplyQuestionComments
from posts.models import Posts
from django.contrib.auth.models import User





# Create your views here.
class CreateCommentPost(CreateView):
	model=PostComments
	fields=['contents']
	template_name='comments/postcomment.html'

	def form_valid(self,form):
		form.instance.author=self.request.user
		print(self.request.user)
		print(self.kwargs)
		form.instance.post=Posts.objects.get(pk=self.kwargs['post_pk'])
		self.object=form.save(commit=False)
		con=self.object.contents
		con=self.check(con)
		self.object.contents=con
		form.save(commit=True)
		return super().form_valid(form)

	def check(self,con):
		final=[]
		s=''
		con="aaa "+con +' aaaaa'+'@'+' '
		n=0
		start=0
		end=0
		user_list=[]
		my_users=User.objects.all()

		for user in my_users:
			user_list.append(user.username)
		print(user_list)


		for i in range(len(con)):
			if n%2==0:
				ch='@'
			else:
				ch=' '

			if con[i]==ch:
				end=i-1
				final.append(con[start:end+1])
				n=n+1
				start=i

		for y in range(len(final)):
			if final[y][0]=='@' and final[y][1:] in user_list:
				user_obj=User.objects.get(username=final[y][1:])
				print(user_obj)
				final[y]="<a href=\"/accounts/user_profile/"+str(user_obj.pk)+"\">"+final[y]+"</a>"
		for y in final:
			s=s+y

		s=s[4:len(s)-6]


		return(s)







class CreateCommentQuestion(CreateView):
	model=QuestionComments
	fields=['contents']
	template_name='questioncomment.html'

	def form_valid(self,form):
		form.instance.author=self.request.user
		print(self.request.user)
		print(self.kwargs)
		form.instance.que=Question.objects.get(pk=self.kwargs['que_pk'])
		return super().form_valid(form)

	def form_valid(self,form):
		form.instance.author=self.request.user
		print(self.request.user)
		print(self.kwargs)
		form.instance.que=Question.objects.get(pk=self.kwargs['que_pk'])
		self.object=form.save(commit=False)
		con=self.object.contents
		con=self.check(con)
		self.object.contents=con
		form.save(commit=True)
		return super().form_valid(form)

	def check(self,con):
		final=[]
		s=''
		con="aaa "+con +' aaaaa'+'@'+' '
		n=0
		start=0
		end=0
		user_list=[]
		my_users=User.objects.all()

		for user in my_users:
			user_list.append(user.username)
		print(user_list)


		for i in range(len(con)):
			if n%2==0:
				ch='@'
			else:
				ch=' '

			if con[i]==ch:
				end=i-1
				final.append(con[start:end+1])
				n=n+1
				start=i

		for y in range(len(final)):
			if final[y][0]=='@' and final[y][1:] in user_list:
				user_obj=User.objects.get(username=final[y][1:])
				print(user_obj)
				final[y]="<a href=\"/accounts/user_profile/"+str(user_obj.pk)+"\">"+final[y]+"</a>"
		for y in final:
			s=s+y

		s=s[4:len(s)-6]


		return(s)




class ReplyComment(CreateView):
	model=ReplyPostComments
	fields=['contents']
	template_name='replycomment.html'

	def form_valid(self,form):
		form.instance.author=self.request.user
		print(self.request.user)
		print(self.kwargs)
		form.instance.comment=PostComments.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)




class ReplyQuestion(CreateView):
	model=ReplyQuestionComments
	fields=['contents']
	template_name='replyquestion.html'

	def form_valid(self,form):
		form.instance.author=self.request.user
		print(self.request.user)
		print(self.kwargs)
		form.instance.post=QuestionComments.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)




