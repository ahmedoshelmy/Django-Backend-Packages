# userapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer
from django.contrib.auth import authenticate
from rest_framework import generics
from packages.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        try:
            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']
                user = User.objects.get(email=email)
            if user is not None:
                if password == user.password:  # An encryption should be added here
                    # a token should be returned (e.g. JWT)
                    return Response({'detail': 'Login successfully.'}, status=status.HTTP_201_CREATED)

        except:
            return Response({'detail': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            if User.objects.filter(email=email).exists():
                return Response({'detail': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new user
            user = User(email=email)
            user.password = password  # Encrypt the password
            user.save()

            return Response({'detail': 'Registration successful.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionsView(generics.ListAPIView):
    serializer_class = PackageSerializer

    def get(self, request, *args, **kwargs):
        email = request.data['email']
        user = User.objects.get(email=email)
        packages = PackageSerializer(user.packages.all(), many=True)
        return JsonResponse(packages.data,
                            status=status.HTTP_200_OK, safe=False)


class AddPackagesToUserView(generics.CreateAPIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            email = request.data['email']
            user = User.objects.get(email=email)
            package_ids = request.data.get('package_ids', [])
            packages = Package.objects.filter(pk__in=package_ids)
            user.packages.add(*packages)
            return JsonResponse({'message': 'Packages added successfully'})
        except Package.DoesNotExist:
            return JsonResponse({'error': 'One or more packages do not exist'}, status=400)
        except:
            return Response({'detail': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
