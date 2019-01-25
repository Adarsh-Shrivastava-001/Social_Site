from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,TemplateView,DetailView
from .models import Question,Answer
from django.shortcuts import redirect,reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from groups.models import Groups
from .forms import AnswerForm
# Create your views here.


class CreateQue(CreateView):
	model=Question
	template_name="qanda/createque.html"
	fields=['que']
	
	def form_valid(self,form):
		form.instance.author=self.request.user
		form.instance.group=Groups.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)






class ListQue(ListView):
	model=Question
	template_name="qanda/ListQue.html"

	def get_queryset(self,**kwargs):
		group=Groups.objects.get(pk=self.kwargs['pk'])
		ques=Question.objects.filter(group=group)
		return ques




class DetailQue(DetailView):
	model=Question
	template_name="qanda/view.html"
	pk_url_kwarg="que_pk"

	def get_context_data(self,**kwargs):
		context=super(DetailView,self).get_context_data(**kwargs)
		context['ans_list']=Answer.objects.filter(que=self.object)
		return context




class CreateAns(CreateView):
	model=Answer
	template_name="qanda/createans.html"
	form_class=AnswerForm
	def form_valid(self,form):
		form.instance.author=self.request.user
		form.instance.que=Question.objects.get(pk=self.kwargs['que_pk'])
		return super().form_valid(form)























