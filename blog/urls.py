from django.contrib import admin
from django.urls import include, path
from blog import views

urlpatterns = [
   #aPi to post comments
   path('postComment',views.postComment, name="postComment"),

   path('',views.blogHome, name='blogHome'),
   path('<str:slug>',views.blogPost, name='blogPost'),

   


      
]
#<str:slug> is to pass query through serach bar