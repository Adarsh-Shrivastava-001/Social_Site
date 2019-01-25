from django.shortcuts import render,redirect
from . forms import UserForm, ProfileForm
from . models import Profile
from PIL import Image
from django.contrib.auth import login, authenticate
from groups.models import Groups
from posts.models import Posts
from django.contrib.auth.models import User



# Create your views here.


def signup(request):

	if request.method=='POST':


		profileform=ProfileForm(request.POST,request.FILES)
		userform=UserForm(request.POST,request.FILES)

		if profileform.is_valid() and userform.is_valid():
			user=userform.save()
			user.set_password(user.password)
			user.save()
			profile=profileform.save(commit=False)
			profile.user=user
			profile.signed=True

			if 'pic' in request.FILES:
				profile.pic=request.FILES['pic']

			else:
				print('no pic')

			profile.save()
			username = userform.cleaned_data.get('username')
			password = userform.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			login(request,user)
			print(username)
			print(password)
			return redirect('home')
            

		else:
			print("The form is invalid")

	else:
		profileform=ProfileForm()
		userform=UserForm()


	
	return render(request,'accounts/signup.html',{'user':userform,'profile':profileform},)



def profile(request):
	posts=Posts.objects.filter(author=request.user)
	admin_groups=Groups.objects.filter(admin=request.user)
	context={'posts':posts,'admin_groups':admin_groups}
	return render(request, template_name='accounts/profile.html',context=context)

def user_profile(request,pk):
	user1=User.objects.get(pk=pk)
	posts=Posts.objects.filter(author=user1)
	admin_groups=Groups.objects.filter(admin=user1)
	context={'posts':posts,'admin_groups':admin_groups,'user':user1}
	return render(request, template_name='accounts/profile.html',context=context)



def drafts(request):
	posts=Posts.objects.filter(date_published=None)
	context={'posts':posts}
	return render(request, template_name='accounts/drafts.html',context=context)











