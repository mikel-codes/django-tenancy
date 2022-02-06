from rest_framework.serializers import serializers
from .models import Poll

class PollSerializer(serializers.ModelSerializer):
    model = Poll
    fields = '__all__'

