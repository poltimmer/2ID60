from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^examples/$', views.examples, name='examples'),
    url(r'^newUser/$', views.newUser, name='newUser'),
    url(r'^discover/$', views.discover, name='discover'),
    url(r'^photogallery/$', views.photogallery, name='photogallery'),
    url(r'^jobgallery/$', views.jobgallery, name='jobgallery'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^upload2/$', views.upload2, name='upload2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
