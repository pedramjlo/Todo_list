from rest_framework import serializers

from .models import Category, Task



class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['is_pinned', 'title', 'date_created', 'category', 'user']

