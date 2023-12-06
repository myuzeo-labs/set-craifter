from django.urls import path
from . import views

urlpatterns = [
    path('tracks/', views.track_list, name='track-list'),
    path('tracks/<int:pk>/', views.track_detail, name='track-detail'),
    path('playlists/', views.playlist_list, name='playlist-list'),
    path('playlists/<int:pk>/', views.playlist_detail, name='playlist-detail'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
]
