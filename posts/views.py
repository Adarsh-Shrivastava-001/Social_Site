from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,TemplateView,DetailView
from .models import Posts
from django.shortcuts import redirect,reverse,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from groups.models import Groups
from django.utils import timezone
from comments.models import PostComments
# Create your views here.


class CreatePost(CreateView):
	model=Posts
	template_name="Posts/createpost.html"
	fields=['title','tag','content']


	def form_valid(self,form):
		form.instance.author=self.request.user
		print(self.request.user)
		print(self.kwargs)
		form.instance.group=Groups.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)



class ListPost(ListView):
	model=Posts
	template_name="Posts/listpost.html"



class DeletePost(DeleteView):
	model=Posts
	template_name="Posts/deletepost.html"
	pk_url_kwarg='post_pk'
	success_url=reverse_lazy('posts:list')


class UpdatePost(UpdateView):
	model=Posts
	template_name="Posts/updatepost.html"
	pk_url_kwarg='post_pk'
	fields=['title','tag','content']






class DetailPost(DetailView):
	model=Posts
	template_name="Posts/detailpost.html"
	pk_url_kwarg='post_pk'

	
	def get_context_data(self,**kwargs):
		context=super(DetailView,self).get_context_data(**kwargs)
		post=self.object
		context['comment_list']=PostComments.objects.filter(post=self.object)
		print(context['comment_list'])
		return context


	

def publish(request,post_pk):
	post=get_object_or_404(Posts,pk=post_pk)
	post.date_published=timezone.now()
	post.save()
	return redirect('posts:detail',post_pk=post_pk)

def like(request,post_pk):
	post=get_object_or_404(Posts,pk=post_pk)

	if request.user not in post.liked_by:
		post.liked_by.add(request.user)
		post.likes=post.likes+1
		post.save()
	else:
		post.liked_by.remove(request.user)
		post.likes=post.likes-1
		post.save()
		
	return redirect('posts:detail',post_pk=post_pk)

