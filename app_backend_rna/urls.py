from django.urls import path
from app_backend_rna.views.audio_view import create_audio, list_audio, get_audio, delete_audio
from app_backend_rna.views.transcription_view import create_transcription, list_transcription, get_transcription, update_transcription, delete_transcription

urlpatterns = [
    path('create_audio/', create_audio, name='create_audio'),
    path('list_audio/', list_audio, name="list_audio"),
    path('get_audio/<int:audio_id>/', get_audio, name="get_audio"),
    path('delete_audio/<int:audio_id>/', delete_audio, name='delete_audio'),

    path('create_transcription/', create_transcription, name='create_transcription'),
    path('list_transcription/', list_transcription, name='list_transcription'),
    path('get_transcription/<int:transcription_id>/', get_transcription, name='get_transcription'),
    path('update_transcription/<int:transcription_id>/', update_transcription, name='update_transcription'),
    path('delete_transcription/<int:transcription_id>/', delete_transcription, name='delete_transcription')
]