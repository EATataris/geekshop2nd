from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm


def login(request):
    title = 'GeekShop - Авторизация'
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    context = {'title': title, 'form': form}
    return render(request, 'users/login.html', context)



def registration(request):
    return render(request, 'users/register.html')