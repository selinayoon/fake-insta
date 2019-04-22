from django.shortcuts import render, redirect
from .forms import PostForm, ImageForm, CommentForm
from .models import Post, Comment, Hashtag
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def list(request):
    posts = Post.objects.all()
    comment_form = CommentForm() #댓글 폼 보여주기
    return render(request, 'posts/list.html',{'posts':posts,'comment_form':comment_form})

#로그인을 하지 않으면 접근할 수 없다.
@login_required   

def create(request):
    #get 작성 폼 보여줄게post 작성한 내용 저장해줄게
    #1. get방식으로 데이터를 입력할 form을 요청한다.
    #4. 사용자가 데이터를 입력해서 post방식으로 요청한다.
    #9.사용자가 다시 적절한 데이터를 입력해서 post방식으로 요청한다.
    
    #저장을 하는지, 폼을 보여주는지 판단. get:폼 보여주기, post:저장하기
    if request.method == "POST":
        
        #5. post방식으로 저장요청을 받고, 데이터를  받아 postform에 넣어서 인스턴스화 한다.
        #10. 5번과 같음
        #request.POST:input안에 있는 데이터
        # 사진 데이터 넣기 사용자가 작성한 정보, 파일 넣기
        #form = PostForm(request.POST, request.FILES)
        
        #수정
        #post폼에다 post정보만
        #이미지 폼에다 이미지 정보만 따로다로 넣게 수정
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST,request.FILES)
        
        
        #6.검증 작업으로 form에 데이터가 제대로 들어왔는지 확인
        #11. 6번과 같음
        if post_form.is_valid():
            # 12. 적절한 데이터가 들어온다. 데이터를 저장하고 list페이지로 리다이렉트!!
            post = post_form.save(commit=False) #게시물 내용만 저장.
            post.user = request.user
            post.save()
            
            post
            
            
            # 파일 안에있는 이미지 가져오기(리스트 형태로), 이미지 출력하기
            #이미지를 따로따로따로 
            #1:N관계
            # 글이 생성된 후, 해당글과 해시태그를 연결시켜야하므로 포스트를 저장한 후에 작업 진행.
            content = post_form.cleaned_data.get('content')
            content_words = content.split()
            for word in content_words:
                if word[0] == "#":
                    tag = Hashtag.objects.get_or_create(content=word) #인 값이 있으면 가져오거나 생성
                    #content 값이 있고, 가져와졌다고 하면, 방금 생성된 post에 hashtag에대가 add한다 tag를
                    post.hashtag.add(tag[0]) #해시태그 추가
            
            
            
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageForm(request.POST, request.FILES)
                #이미지 아닌거 거르기
                if image_form.is_valid():
                    image = image_form.save(commit=False)# 잠깐만 기다료
                    image.post = post
                    image.save()
            
            return redirect("posts:list")
        # else:
        #     #7. 데이터 검증을 통과하지 못한 경우
        #     pass # 없어도 무방한 코드
    else:
        #2. PostForm을 인스턴스화(변수화) 시켜서 form에 저장한다.
        post_form = PostForm()
        image_form = ImageForm()
    
    #사용자가 데이터를 잘못입력했을 때, 8은 입력된 데이터를 계속 유지시켜준다.
    #3. form을 담아 create.html로 보내준다.
    #8. 사용자가 입력한 데이터는 form에 담아진 상태로 다시 form을 담아 create.html을 보내준다.
    #postform에는 postform을  imageform에는 imageform을 넣어준다.
    return render(request, 'posts/form.html', {'post_form':post_form,"image_form":image_form})
    

#수정을 하려면 이전의 데이터를 찾아와야한다.
# create 함수와 차이점은 이전의 정보를 가져온다는 것
@login_required
def update(request,id):
    post = Post.objects.get(id=id)
    #get 작성 폼 보여줄게post 작성한 내용 저장해줄게
    if post.user == request.user: # 지금 로그인한 사람이 게시물을 작성해따
        if request.method == "POST":
            form = PostForm(request.POST,instance=post)
            # form에 데이터 넣고 검증하기
            if form.is_valid():
                form.save()
                
                
                post.hashtags.clear() #해시태그를 날린 후 재생성
                content = form.cleaned_data.get('content')
                content_words = content.split()
                for word in content_words:
                    if word[0] == "#":
                        #content 값이 있고, 가져와졌다고 하면, 방금 생성된 post에 hashtag에대가 add한다 tag를
                        tag = Hashtag.objects.get_or_create(content=word) 
                        post.hashtags.add(tag[0])
                return redirect("posts:list")
            # else:
            #     pass 없어도 무방한 코드
        else:
            # 인스턴스로 이 전의 데이터 가져옴  
            form = PostForm(instance=post)
        return render(request, 'posts/form.html',{'form':form})
    else:
        return redirect("posts:list")
# 삭제하기
@login_required
def delete(request,id):
    # 지우고싶은 게시물 찾기
    post = Post.objects.get(id=id)
    # 로그인한 유저랑 게시물 작성유저랑 같은지 확인
    if post.user == request.user:
        post.delete()
        return redirect("posts:list")
    else:
        return redirect("posts:list")
    
    
#댓글 달기
@login_required
def comment_create(request, post_id):
    #댓글 작성 폼을 list에서 보여줄거임.
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        # 폼에 데이터 잘 들어갔는지 검증, save
        if comment_form.is_valid():
            comment = comment_form.save(commit= False) #유저정보,몇번 글 넣어야하니까 기다려
            #유저정보
            comment.user = request.user
            #몇번 글에 작성할건지
            comment.post = Post.objects.get(id=post_id)#포스트 번호
            comment.save() # auto_now_add 를 이미 줘서 그냥 저장됨.
            return redirect('posts:list')
    # else:
    #     pass 필요없음

#댓글 삭제하기\
# 삭제하기
@login_required
def comment_delete(request,post_id,comment_id):
    # 코멘트
    comment = Comment.objects.get(id=comment_id)
    #코멘트를 작성한 유저랑 요청 유저랑 같은지 확인.
    if comment.user == request.user:
        comment.delete()
    return redirect("posts:list")
    
#과거의 코드
# @login_required
# def like(request,id):
#     user = request.user # 좋아요 누르는 유저 정보
#     post = Post.objects.get(id=id)
#     # 사용자가 좋아요를 안눌렀다면
#     #     좋아요 추가
#     # 사용자가 좋아요를 이미 눌렀다면
#     #     좋아요 취소
    
#     likes = post.like_set.all()
#     for like in likes:
#         if user == like.user:
#             #사용자가 이미 눌렀으 때
#             check = 1
#             like_post = like
#     if check ==1:
#         like_post.delete()
#     else:
#         #사용자가 안눌렀을 때            
#         like = Like(user=user,post=post)
#         like.save()
#     return redirect('posts:list')

@login_required
def like(request,id):
    user = request.user
    post = Post.objects.get(id=id)
    
    # 사용자가 좋아요를 눌렀다면
    # if 사용자 in 좋아요 목록
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        # 사용자가 좋아요를 누르지 않았다면
        post.likes.add(user)
    return redirect('posts:list')
        
        
def hashtag(request, id):
    hashtag = Hashtag.objects.get(id=id)
    posts = hashtag.post_set.all()
    comment_form = CommentForm()
    
    return render(request, 'posts/list.html', {"posts":posts, "comment_form":comment_form, "hashtag":hashtag})