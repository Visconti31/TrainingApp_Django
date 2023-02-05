from rest_framework.serializers import ModelSerializer

from .models import Exercise

# Take the python class and return a JSON response

class ExerciseSerializer(ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'