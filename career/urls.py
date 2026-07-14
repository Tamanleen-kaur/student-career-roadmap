from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('career_list/',views.career_list,name='career_list'),
     path("career/<int:id>/",views.career_details,name="career_details"),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.login_view,name='login'),
    path('profile/',views.profile,name='profile'),
    path('quiz/',views.quiz,name='quiz'),
    path('register/',views.register,name='register'),
    path('resources/',views.resources,name='resources'),
    path('roadmap/',views.roadmap,name='roadmap'),
     path('dashboard/',views.dashboard,name='dashboard'),
     path('quiz/',views.quiz,name='quiz'),
      path('resources/',views.resources,name='resources'),
      path('profile/',views.profile,name='profile'),
       path('progress/',views.progress,name='progress'),
       path('logout/',views.logout_view,name="logout"),
       path("roadmap/<int:career_id>/", views.roadmap, name="roadmap"),

]
