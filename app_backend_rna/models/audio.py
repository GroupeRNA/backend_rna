from django.db import models

class Audio(models.Model):
    audio_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='audio/')
    audio_title = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
