from django.conf.urls import url,include
from .import views

app_name='qanda'

urlpatterns = [
    url(r'^$', views.ListQue.as_view() , name="list"),
	url(r'^ask/$', views.CreateQue.as_view() , name="ask"),
	url(r'^detail/(?P<que_pk>\d+)$', views.DetailQue.as_view() , name="detail"),
    url(r'^detail/(?P<que_pk>\d+)/ans', views.CreateAns.as_view() , name="createans")

]