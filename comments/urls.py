from django.conf.urls import url,include
from .import views

app_name='comments'

urlpatterns = [
    url(r'^createcommentpost/', views.CreateCommentPost.as_view() , name="postcreatecomment"),
    url(r'^createcommentquestion/', views.CreateCommentQuestion.as_view() , name="createcommentquestion"),
    url(r'^createcommentpost/', views.ReplyComment.as_view() , name="replycomment"),
    url(r'^createcommentpost/', views.ReplyQuestion.as_view() , name="replyquestion"),

       

]