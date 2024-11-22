from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
# Create your views here.


class UserApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        
        new_user = {
            "username": request.data.get('username'),
            "email": request.data.get('email'),
        }
        
        serializer = UserSerializer(data=new_user)
        # .strftime("%d-%m-%Y, %H:%M:%S")
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)