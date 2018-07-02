"""myblog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/(?P<id>\d+)/$', views.post_detail, name='detail'),    
    url(r'^posts/create/$', views.post_create),
    url(r'^posts/(?P<id>\d+)/delete/$', views.post_delete),
    url(r'^posts/(?P<id>\d+)/edit/$', views.post_update,  name='update'),
    url(r'^posts/$', views.post_list, name='list')
]