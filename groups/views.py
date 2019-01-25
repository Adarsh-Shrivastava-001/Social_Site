from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,TemplateView,DetailView
from .models import Groups
from django.shortcuts import redirect,reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from posts.models import Posts

# Create your views here.


class CreateGroup(CreateView):
	model=Groups
	template_name="Groups/CreateGroup.html"
	fields=['name','tag','description','pic','hidden']
	
	def form_valid(self,form):
		form.instance.admin=self.request.user
		return super().form_valid(form)






class ListGroup(ListView):
	model=Groups
	template_name="Groups/listgroup.html"

class DeleteGroup(DeleteView):
	model=Groups
	template_name="Groups/deletegroup.html"
	success_url=reverse_lazy('groups:list')


class DetailGroup(DetailView):
	model=Groups
	template_name="Groups/detailgroup.html"

	def get_context_data(self,**kwargs):
		context=super(DetailView,self).get_context_data(**kwargs)
		group=self.object
		context['post_list']=Posts.objects.filter(group=self.object)
		return context



def joingroup(request,pk):
	group=Groups.objects.get(pk=pk)
	group.members.add(request.user)
	group.save()
	return redirect('groups:detail',pk=group.pk)

