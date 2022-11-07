from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('bar/',views.bar,name = 'bar'),
    path('spider/',views.spider,name = 'spider'),
    path('convert/',views.convert,name = 'conversion')
]


