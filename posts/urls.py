from django.conf.urls import url,include
from .import views

app_name='posts'

urlpatterns = [
    url(r'^create/', views.CreatePost.as_view() , name="create"),
    url(r'^detail/(?P<post_pk>\d+)/delete$', views.DeletePost.as_view() , name="delete"),
    url(r'^detail/(?P<post_pk>\d+)/update$', views.UpdatePost.as_view() , name="update"),
    url(r'^list/', views.ListPost.as_view() , name="list"),
    url(r'^detail/(?P<post_pk>\d+)$', views.DetailPost.as_view() , name="detail"),
    url(r'^detail/(?P<post_pk>\d+)/publish/', views.publish , name="publish"),
    url(r'^detail/(?P<post_pk>\d+)/comment/', include('comments.urls', namespace='comment')),
    url(r'^detail/(?P<post_pk>\d+)/like/', views.like , name="like"),    

]

