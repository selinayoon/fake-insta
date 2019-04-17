from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        #내가 만든 폼 사용하기
        form = CustomUserCreationForm(request.POST)
        #유효성 검사
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = CustomUserCreationForm()
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
    
#유저 페이지
def user_page(request, id):
    User = get_user_model()
    user_info = User.objects.get(id=id)
    return render(request, "accounts/user_page.html",{'user_info':user_info})
    
#follow 기능

# @login_required
def follow(request,id):
    User = get_user_model()
    me = request.user
    you = User.objects.get(id=id)
    
     # me:로그인한사람 you:팔로우버튼을 누른사람
    if me != you:
        if you in me.followings.all(): #너가 내 팔로잉 하고있니?
            me.followings.remove(you)
        else:
            me.followings.add(you)
    return redirect("accounts:user_page", id)
            
#프로필 수정
@login_required
def edit_profile(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    if user == request.user:
        if request.method=="POST":
            # form = CustomUserChangeForm(request.POST)
            # 이메일정보,이미지정보 넣기
            form = CustomUserChangeForm(request.POST,request.FILES,instance=user)
            if form.is_valid():
                form.save()
                return redirect('accounts:user_page',id)
        else:
            form = CustomUserChangeForm(instance=user)
        return render(request,'accounts/form.html',{'form':form})
    return redirect('accounts:login')
