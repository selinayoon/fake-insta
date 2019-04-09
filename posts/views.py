from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html',{'posts':posts})
    
def create(request):
    #1. get방식으로 데이터를 입력할 form을 요청한다.
    #4. 사용자가 데이터를 입력해서 post방식으로 요청한다.
    #9.사용자가 다시 적절한 데이터를 입력해서 post방식으로 요청한다.
    
    #저장을 하는지, 폼을 보여주는지 판단. get:폼 보여주기, post:저장하기
    if request.method == "POST":
        
        #5. post방식으로 저장요청을 받고, 데이터를  받아 postform에 넣어서 인스턴스화 한다.
        #10. 5번과 같음
        #request.POST:input안에 있는 데이터
        # 사진 데이터 넣기
        form = PostForm(request.POST, request.FILES)
        #6.검증 작업으로 form에 데이터가 제대로 들어왔는지 확인
        #11. 6번과 같음
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        # else:
        #     #7. 데이터 검증을 통과하지 못한 경우
        #     pass # 없어도 무방한 코드
    else:
        #2. PostForm을 인스턴스화(변수화) 시켜서 form에 저장한다.
        form = PostForm()
    
    #사용자가 데이터를 잘못입력했을 때, 8은 입력된 데이터를 계속 유지시켜준다.
    #3. form을 담아 create.html로 보내준다.
    #8. 사용자가 입력한 데이터는 form에 담아진 상태로 다시 form을 담아 create.html을 보내준다.
    return render(request, 'posts/form.html',{'form':form})
    

#수정을 하려면 이전의 데이터를 찾아와야한다.
# create 함수와 차이점은 이전의 정보를 가져온다는 것 
def update(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        # form에 데이터 넣고 검증하기
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        # else:
        #     pass 없어도 무방한 코드
    else:
        # 인스턴스로 이 전의 데이터 가져옴  
        form = PostForm(instance=post)
    return render(request, 'posts/form.html',{'form':form})
    
# 삭제하기
def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("posts:list")