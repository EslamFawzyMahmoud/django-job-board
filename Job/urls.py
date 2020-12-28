from django.contrib import admin
from django.urls import path ,include
from . import views

app_name='Job'
#name --> to arrive to the page
urlpatterns = [
    path('',views.Job_List,name='job_list'),
    path('add', views.add_job, name="add_job"),
    path('<str:slug>',views.Job_Detail,name="job_detail"),
]
