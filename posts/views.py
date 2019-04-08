from django.shortcuts import render,redirect
from .forms import PostForm


# Create your views here.
def list(request):
    return render(request, 'posts/list.html')
    
def create(request):
    #1. get방식으로 데이터를 입력할 form을 요청한다.
    #4. 사용자가 데이터를 입력해서 post방식으로 요청한다.
    #9.사용자가 다시 적절한 데이터를 입력해서 post방식으로 요청한다.
    if request.method == "POST":
        #5. post방식으로 저장요청을 받고, 데이터를  받아 postform에 넣어서 인스턴스화 한다.
        #10. 5번과 같음
        #request.POST:input안에 있는 데이터
        form = PostForm(request.POST)
        #6.검증 작업으로 form에 데이터가 제대로 들어왔는지 확인
        #11. 6번과 같음
        if form.is_valid():
            form.save
            return redirect("posts:list")
        else:
            #7. 데이터 검증을 통과하지 못한 경우
            pass
    else:
        #2. PostForm을 인스턴스화(변수화) 시켜서 form에 저장한다.
        form = PostForm()
    
    #사용자가 데이터를 잘못입력했을 때, 8은 입력된 데이터를 계속 유지시켜준다.
    #3. form을 담아 create.html로 보내준다.
    #8. 사용자가 입력한 데이터는 form에 담아진 상태로 다시 form을 담아 create.html을 보내준다.
    return render(request, 'posts/create.html',{'form':form})