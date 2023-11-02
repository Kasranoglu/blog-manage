from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from .serializer import UserSerializer
from rest_framework.response import Response


# Create your views here.
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def post(self, request, format=None):
        if request.user.is_authenticated:
            # Kullanıcının sahip olduğu tokeni al
            token, created = Token.objects.get_or_create(user=request.user)

            # Tokeni sil
            token.delete()

            return Response({"success": "Token deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):

    def post(self, request):
        # İstekten gelen verileri alın
        data = request.data

        # Verileri UserSerializer kullanarak doğrulayın ve kaydolun
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'message': 'Kullanıcı kaydı başarıyla tamamlandı.',
                'user_data': serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)