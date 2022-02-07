"""mini_web_creator_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from main import views

condition = True


def the_url():
    if condition:
        return path('', views.base)


app_name = 'main'
urlpatterns = [
    path('', views.base),
    path('section/<str:slug>/', views.section, name='section'),
    path('section/<str:slug>/<str:post_slug>/', views.post_details, name='details'),
    path('section/<str:slug>/gallery/<int:pk>/', views.gallery_details, name='gallery_details'),
    path('gallery1/', views.gallery1, name='gallery1'),
    path('gallery2/', views.gallery2, name='gallery2'),
    path('gallery3/', views.gallery3, name='gallery3'),
    path('test/', views.testing_post, name='testing_post'),
    path('post1/', views.post1, name='post1'),
    path('post2/', views.post2, name='post2'),
    path('post3/', views.post3, name='post3'),

]

# path('<str:slug_post>/', posts_views.details, name='details'),
