"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from . import views

handler500 = 'learn_django.views.page_500'
handler404 = 'learn_django.views.page_404'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/$', views.index),
    url(r'^article/(?P<year>\d{4})/$', views.article, name='article_detail'),
    # url(r'^auth/', include('oauth.urls', namespace='auth')),
    url(r'^$', views.index, name='index'),
    url(r'^index1/one/$', views.index_one, name='index_one'),
    url(r'^index2/$', views.index_two, name='index_two'),


    #打印请求对象
    url(r'^print/request/$', views.print_request, name='print_request'),
    url(r'mall/', include('mall.uls', namespace='mall')),
]



# 添加自定义的静态资源目录访问
urlpatterns += [url(r'^medias/(?P<path>.*)$',serve, {
    'document_root': settings.MEDIA_ROOT
})]

