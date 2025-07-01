from django.db import models
from app_backend_rna.models.user import User

class Audio(models.Model):
    audio_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='audio/')
    audio_title = models.CharField(max_length=100)
    audio_url = models.CharField(max_length=50, null=True)
    transcription = models.TextField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)