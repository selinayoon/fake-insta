from django import template

register = template.Library()

@register.filter
# 요 함수는 가지고 있는 content의 정보를 가져와서 다 자른다
def hashtag_link(post):
    content = post.content # #하이 #안녕 처럼 스트링의 덩어리가 들어감
    hashtags = post.hashtag.all() # <queryset [hashtag1, hashtag6]>
    
    #하이 라는 문장을 <a href='<% url '' %>'>하이</a> 식으로 바꾸기
    for hashtag in hashtags:
        content = content.replace(f"{hashtag.content}", f"<a href='/posts/hashtag/{hashtag.id}/'>{hashtag.content}</a>")
        
    return content