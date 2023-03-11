"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.views.static import serve
from django.urls import path
import xadmin

from articles.views import Index, CategoriesView, ArticlesView, ContactView, MsgView, SearchView, AddFavView

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('', Index.as_view(), name='index'),
    path('categories/<int:pk>/', CategoriesView.as_view(), name='categories'),   # 文章分类列表
    path('article/<int:pk>/', ArticlesView.as_view(), name='article'),    # 文章详情
    path('contact/', ContactView.as_view(), name='contact'),    # 联系我
    path('search/', SearchView.as_view(), name='search'),   # 搜索
    path('msg/', MsgView.as_view(), name='msg'),   # 留言
    url('^addfav/(?P<pk>\d+)/$', AddFavView.as_view(), name='addfav'),   # 点赞
    url(r'^ueditor/', include('DjangoUeditor.urls')),

]

if settings.DEBUG:
    #  配置静态文件访问处理
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))
    urlpatterns.append(url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}))