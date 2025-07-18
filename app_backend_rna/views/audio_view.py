from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from app_backend_rna.models.audio import Audio
from rest_framework.permissions import IsAuthenticated
import whisper


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_audio(request):
    user = request.user

    audio_file = request.FILES.get('file')
    audio_title = request.data.get('audio_title')
    audio_url = request.data.get('audio_url')


    if not audio_file or not audio_title:
        return Response({'error': 'Aucun fichier audio fourni'}, status=400)
    
    audio = Audio.objects.create(user=user, file=audio_file, audio_title=audio_title, audio_url=audio_url)

    model = whisper.load_model("base")
    result = model.transcribe(audio.file.path)

    audio.transcription = result["text"]
    audio.save()

    return Response({
        "audio_id": audio.audio_id,
        "uploaded_at" : audio.uploaded_at,
        "audio_title": audio.audio_title,
        "audio_url": audio.audio_url,
        "transcription": audio.transcription,
        "file_url": audio.file.url
    }, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_audio(request):
    audios = Audio.objects.all()
    audio_list = [
        {
            "audio_id": audio.audio_id,
            "audio_title": audio.audio_title,
            "file": audio.file.url,
            "uploaded_at": audio.uploaded_at,
            "transcription": audio.transcription
        } for audio in audios
    ]

    return Response(audio_list)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_audio_by_user(request):
    user = request.user
    try:
        audio = Audio.objects.get(user=user)
    except Audio.DoesNotExist:
        return Response({'error': 'Audio non trouvé'}, status=404)
    
    return Response({
        "audio_id": audio.audio_id,
        "audio_title": audio.audio_title,
        "file": audio.file.url,
        "transcription": audio.transcription,
        "uploaded_at": audio.uploaded_at
    })

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_audio(request, audio_id):
    try:
        audio = Audio.objects.get(audio_id=audio_id)
    except Audio.DoesNotExist:
        return Response({'error': 'Audio non trouvé'}, status=404)
    
    audio.delete()

    return Response({'message': 'Audio supprimer'})