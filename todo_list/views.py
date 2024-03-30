from django.shortcuts import render

from .models import Task, Category
from .serializers import CategorySerializer, TaskSerializer

from rest_framework import status, authentication, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User





class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response({'message': 'Task was created successfully'}, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response({'message': 'Category was created successfully'}, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class GetTasks(APIView):

    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        tasks = [f"{task.user}: {task.title}" for task in Task.objects.all()]
        return Response(tasks)



class GetCategories(APIView):

    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        categories = [f"{category.user}: {category.name}" for category in Category.objects.all()]
        return Response(categories)
    


class GetTask(APIView):
    permission_class = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            task = Task.objects.get(id=kwargs['pk'])
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class GetCategory(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(id=kwargs['pk'])
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    


class UpdateTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
    

class UpdateCategory(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_class = [permissions.AllowAny,]



class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class = [permissions.AllowAny,]
