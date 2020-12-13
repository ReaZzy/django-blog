from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserOurRegistration, ProfileImage, UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserOurRegistration(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Користувач {username} усішно зареєстрований, введіть логін та пароль для авторизації')
			return redirect('auth')
	else:
		form = UserOurRegistration()
	return render(request, 'users/registrations.html', {"form":form, 'title':'Реєстрація'})

@login_required
def profile(request):
	if request.method == 'POST':
		img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
		update_user = UserUpdateForm(request.POST,instance=request.user)

		if update_user.is_valid() and img_profile.is_valid():
			update_user.save()
			img_profile.save()
			messages.success(request, 'Ваш аккаунт успішно оновлено')
			return redirect('profile')

	else:
		img_profile = ProfileImage(instance=request.user.profile)
		update_user = UserUpdateForm(instance=request.user)

	data={'img_profile':img_profile, 'update_user':update_user}

	return render(request, 'users/profile.html', data)