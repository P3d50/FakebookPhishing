from django.urls import path
from . import views

urlpatterns = [
    path('facebook/', views.fakebookLogin, name='facebook'),
    path('facebook/hacked', views.hacked, name='hacked'),

]
