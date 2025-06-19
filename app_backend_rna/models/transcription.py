from django.db import models
from app_backend_rna.models.audio import Audio

class Transcription(models.Model):
    transcription_id = models.AutoField(primary_key=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    transcription_title = models.CharField(max_length=100)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)