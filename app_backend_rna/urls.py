from django.urls import path
from app_backend_rna.views.audio_view import create_audio, list_audio, get_audio_by_user, delete_audio
from app_backend_rna.views.auth_view import register, login, get_user_by_id

urlpatterns = [
    path('create_audio/', create_audio, name='create_audio'),
    path('list_audio/', list_audio, name="list_audio"),
    path('get_audio_by_user/', get_audio_by_user, name="get_audio_by_user"),
    path('delete_audio/<int:audio_id>/', delete_audio, name='delete_audio'),

    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('get_user_by_id/', get_user_by_id, name='get_user_by_id')
]