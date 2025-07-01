from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from app_backend_rna.models.user import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def register(request):
    user_name = request.data.get("user_name")
    user_mail = request.data.get("user_mail")
    user_password = request.data.get("user_password")

    if User.objects.filter(user_name=user_name).exists():
        return Response({'error': "Nom d'utilisateur déjà existe"}, status=400)
    
    user = User.objects.create_user(
        user_name = user_name,
        user_mail = user_mail,
        user_password = user_password
    )

    return Response({'message': "Utilisateur enregistrer"}, status=201)

@api_view(['POST'])
def login(request):
    user_name = request.data.get("user_name")
    user_password = request.data.get('user_password')

    user = authenticate(user_name=user_name, password=user_password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user_id': user.id,
            'user_name': user.user_name,
        })
    else: 
        return Response({'error': "Nom d'utilisateur ou mot de passe invalide"}, status=401)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_by_id(request):
    user = request.user  # ✅ L'utilisateur déjà connecté via le JWT

    return Response({
        "id": user.id,
        "user_name": user.user_name,
        "user_mail": user.user_mail
    })
