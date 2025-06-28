from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from app_backend_rna.models.audio import Audio
from app_backend_rna.models.transcription import Transcription
import whisper
import os
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transcription(request):
    audio_id = request.data.get('audio_id')
    transcription_title = request.data.get('transcription_title')

    if not audio_id or not transcription_title:
        return Response({'error': "audio_id et transcription_title sont requis"}, status=400)
    
    try:
        audio = Audio.objects.get(audio_id=audio_id)
    except Audio.DoesNotExist:
        return Response({'error': 'Audio non trouvé'}, status=404)

    if hasattr(audio, 'transcription'):
        return Response({'error': 'Cette audio a déjà une transcription'}, status=400)
    
    model = whisper.load_model("base")
    result = model.transcribe(audio.file.path)

    transcription = Transcription.objects.create(
        audio=audio,
        text = result["text"],
        transcription_title = transcription_title
    )

    return Response({
        "transcription_id": transcription.transcription_id,
        "text": transcription.text,
        "created_at": transcription.created_at
    }, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_transcription(request):
    transcriptions = Transcription.objects.all()
    transcription_list = [
        {
            "transcription_id": transcription.transcription_id,
            "transcription_title": transcription.transcription_title,
            "text": transcription.text,
            "created_at" : transcription.created_at
        } for transcription in transcriptions
    ]

    return Response (transcription_list)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_transcription(request, transcription_id):
    try:
        transcription = Transcription.objects.get(transcription_id=transcription_id)
    except Transcription.DoesNotExist:
        return Response({'error': 'Transcription non traouvé'}, status=404)
    
    return Response({
        "transcription_id": transcription.transcription_id,
        "transcription_title": transcription.transcription_title,
        "text": transcription.text,
        "created_at" : transcription.created_at
    })

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_transcription(request, transcription_id):
    try:
        transcription = Transcription.objects.get(transcription_id=transcription_id)
    except Transcription.DoesNotExist:
        return Response({'error': 'Transcription non trouvé'}, status=404)
    
    new_title = request.data.get('transcription_title')
    new_text = request.data.get('text')

    if not new_title or not new_text:
        return Response({'error': 'Aucune donnée à mettre à jour'}, status=400)
    
    if new_title:
        transcription.transcription_title = new_title
    
    if new_text:
        transcription.text = new_text

    transcription.save()

    return Response({
        "message": "Transcription mise à jour avec succès",
        "transcription_id": transcription.transcription_id,
        "transcription_title": transcription.transcription_title,
        "text": transcription.text
    })

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_transcription(request, transcription_id):
    try:
        transcription = Transcription.objects.get(transcription_id=transcription_id)
    except Transcription.DoesNotExist:
        return Response({'error': 'Transcription non trouver'}, status=404)
    
    transcription.delete()

    return Response({'message': 'Transcription supprimer'})