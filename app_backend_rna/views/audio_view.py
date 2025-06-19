from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_backend_rna.models.audio import Audio

@api_view(['POST'])
def create_audio(request):
    audio_file = request.FILES.get('file')
    audio_title = request.data.get('audio_title')

    if not audio_file or not audio_title:
        return Response({'error': 'Aucun fichier audio fourni'}, status=400)
    
    audio = Audio.objects.create(file=audio_file, audio_title=audio_title)

    return Response({
        "audio_id": audio.audio_id,
        "uploaded_at" : audio.uploaded_at,
        "audio_title": audio.audio_title,
        "file_url": audio.file.url
    })

@api_view(['GET'])
def list_audio(request):
    audios = Audio.objects.all()
    audio_list = [
        {
            "audio_id": audio.audio_id,
            "audio_title": audio.audio_title,
            "file": audio.file.url,
            "uploaded_at": audio.uploaded_at
        } for audio in audios
    ]

    return Response(audio_list)

@api_view(['GET'])
def get_audio(request, audio_id):
    try:
        audio = Audio.objects.get(audio_id=audio_id)
    except Audio.DoesNotExist:
        return Response({'error': 'Audio non trouvé'}, status=404)
    
    return Response({
        "audio_id": audio.audio_id,
        "audio_title": audio.audio_title,
        "file": audio.file.url,
        "uploaded_at": audio.uploaded_at
    })

@api_view(['DELETE'])
def delete_audio(request, audio_id):
    try:
        audio = Audio.objects.get(audio_id=audio_id)
    except Audio.DoesNotExist:
        return Response({'error': 'Audio non trouvé'}, status=404)
    
    audio.delete()

    return Response({'message': 'Audio supprimer'})