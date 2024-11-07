from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import UserRegistrationSerializer, TweetSerializer
from .models import Tweets
from rest_framework.permissions import IsAuthenticated


class UserRegistrationAPI(APIView):
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TweetCreateAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TweetsListAPI(generics.ListAPIView):
    queryset = Tweets.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

