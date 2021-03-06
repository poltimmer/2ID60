from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [
    #other
    url(r'^$', views.index, name='index'),
    url(r'^', include('api.urls')),
    url(r'^home/$', views.homefeed, name='homefeed'),
    url(r'^static/media/(?P<pk>[a-zA-Z0-9]+)/$', views.download, name='download'),
    url(r'^photogallery/$', views.photogallery, name='photogallery'),

    #login/out/signup
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

    #profiles
    url(r'^myprofile/$', views.myprofile, name='newUser'),
    url(r'^user/(?P<pk>[a-zA-Z0-9]+)/$', views.userprofile, name='userprofile'),
    url(r'^user/(?P<pk>[a-zA-Z0-9]+)/follow/$', views.follow, name='follow'),
    url(r'^user/(?P<pk>[a-zA-Z0-9]+)/unfollow/$', views.unfollow, name='unfollow'),
    url(r'^search/u/(?P<pk>[a-zA-Z0-9_]+)/$', views.usersearch, name='usersearch'),
    url(r'^userlist/$', views.userlist, name='userlist'),

    #uploading/creating posts
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^upload_pp/$', views.upload_pp, name='upload_pp'),
    url(r'^upload_img/$', views.upload_img, name='upload_img'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
