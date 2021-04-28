from rest_framework import fields, serializers
from .models import Poll

class CreatePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class ListActivePollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'