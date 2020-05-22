from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password

# Create your views here.
def index(request):
    return render(request,'login/index.html')

def fail(request):
        if request.method=="POST":
                if request.POST['password1'] == request.POST['password2']:
                        user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
                        auth.login(request, user)
                        return redirect('login:index')
        return render(request,'login/fail.html')

def signup(request):
    if request.method=="POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('login:success')
        else:
            return redirect('login:fail')
    return render(request,'login/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login:loginsuccess')
        else:
            return render(request, 'login/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login:login')
    return render(request, 'login/logout.html')

def success(request):
        return render(request,'login/success.html')       

def loginsuccess(request):
        return render(request,'login/loginsuccess.html')       

def change_pw(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect("login:index")
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "login/change_pw.html",context)