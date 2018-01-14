from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^examples/$', views.examples, name='examples'),
    url(r'^myprofile/$', views.newUser, name='newUser'),
    url(r'^discover/$', views.discover, name='discover'),
    url(r'^photogallery/$', views.photogallery, name='photogallery'),
    url(r'^jobgallery/$', views.jobgallery, name='jobgallery'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^', include('api.urls')),
    url(r'^upload_pp/$', views.upload_pp, name='upload_pp'),
    url(r'^upload_img/$', views.upload_img, name='upload_img'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^userlist/$', views.userlist, name='userlist'),
    url(r'^user/(?P<pk>[a-zA-Z0-9]+)/$', views.userprofile, name='userprofile'),
    url(r'^user/add/$', views.friend_add, name='friend_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
