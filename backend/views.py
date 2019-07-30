from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from backend.serializers import RegisterSerializer, UserSerializer


def login(request):
    return HttpResponse("Hello World!")


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(token, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getProfile(request):
    user = request.user
    serializer = UserSerializer(instance=user)
    return Response(serializer.data, status.HTTP_200_OK)
