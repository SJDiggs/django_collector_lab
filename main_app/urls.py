#All paths specific to motorcyclecollector
from django.urls import path
# eventually we'll be pointed to view functionality which handles our requests and responses
from . import views

urlpatterns = [
    #anticipate there will be a home function within views.py
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('motorcycles/', views.motorcycles_index, name = 'index'),
    path('motorcycles/<int:motorcycle_id>/', views.motorcycles_detail, name = 'detail'),
]