from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from writings.models import Writing
from django.contrib import messages,auth
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def register(request):
	if request.method=='POST':
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created. Now you can log in to your account.')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request,'users/register.html',{'form':form})

def profile(request):
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your profile has been updated!')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form':u_form,
		'p_form':p_form
		}
	return render(request,'users/profile.html',context)

def password_update(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			messages.success(request,f'Your password has been updated!')
			return redirect('profile')

	else:
		form=PasswordChangeForm(user=request.user)
	context={
		'form':form
	}
	return render(request,'users/update_password.html',context)


def logout(request):
	if request.method == "POST":
		auth.logout(request)
		messages.success(request,"you are now logged out")
		return redirect('writings')