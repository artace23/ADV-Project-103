from rest_framework import serializers
from .models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'

    def save(self, **kwargs):
        # Set the user field to the currently logged-in user
        self.validated_data['user'] = self.context['request'].user
        return super().save(**kwargs)