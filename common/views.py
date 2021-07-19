from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .form import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)  # 바로 로그인되어 세션 권한 획득(인증)
            return redirect('index')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)