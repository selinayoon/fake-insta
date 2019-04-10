from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #유효성 검사
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    #유저크리에이션 폼도 같이 넘기기
    #왜 리턴이 바깥에 있는가?
    return render(request, 'accounts/form.html',{'form':form})
    
def login(request):
    if request.method=="POST":
        # 들어온 정보 인스턴스화
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            # 정보 잘 들어왔니?=>로그인 하기(세션에 저장)
            auth_login(request, form.get_user())
            return redirect("posts:list")
    else:
        form = AuthenticationForm() 
    return render(request,'accounts/form.html',{"form":form})

def logout(request):
    auth_logout(request)
    return redirect("posts:list")