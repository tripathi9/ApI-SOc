"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from api.views import AuthRegister
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib.auth import views as auth_views
from api import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^Login', obtain_jwt_token),
    #url(r'^login/$', auth_views.login),
    # url(r'^', include('rest_framework.urls')),
    url(r'^SignUp$', AuthRegister.as_view()),
    url(r'^addFeeds/$', views.post_feed),
    url(r'^feedsLike/$', views.feed_likes),
    url(r'^Login$', views.login),
    url(r'^Allfeeds/$', views.get_all_feeds),
]
