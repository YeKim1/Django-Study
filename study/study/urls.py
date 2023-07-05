"""
URL configuration for study project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from user.views import * 
from post.views import *

# Swagger 설정
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "Swagger 타이틀 작성",
        default_version = "v1",
        description = "Swagger를 사용한 API 문서입니다",
    ),
    public=True,
    permission_classes=(AllowAny,),
    
)

urlpatterns = [
    # Swagger url
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path('signup/', Signup.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('myinfo/', MyInfo.as_view()),
    path('postAPI/', PostAPI.as_view()),
    path('commentAPI/', CommentAPI.as_view()),
    path('Q1/', Q1.as_view()),
    path('Q2/', Q2.as_view()),
    path('Q3/', Q3.as_view()),
    path('Q4/', Q4.as_view()),
    path('Q5/', Q5.as_view()),
    path('Q6/', Q6.as_view()),
    

]

