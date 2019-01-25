from django.conf.urls import url,include
from .import views

app_name='groups'

urlpatterns = [
    url(r'^create/', views.CreateGroup.as_view() , name="create"),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteGroup.as_view() , name="delete"),
    url(r'^list/', views.ListGroup.as_view() , name="list"),
    url(r'^detail/(?P<pk>\d+)$', views.DetailGroup.as_view() , name="detail"),
    url(r'^detail/(?P<pk>\d+)/join/', views.joingroup , name="join"),
    url(r'^detail/(?P<pk>\d+)/post/', include('posts.urls', namespace='post')),
    url(r'^detail/(?P<pk>\d+)/discuss/', include('qanda.urls', namespace='q_and_a')),
       

]

