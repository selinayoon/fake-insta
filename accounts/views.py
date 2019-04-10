from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

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
    return render(request, 'accounts/signup.html',{'form':form})
        