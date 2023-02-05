from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ExerciseSerializer
from .models import Exercise

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/workouts/',
            'method': 'GET',
            'body': None,
            'description': 'Return an array of workouts'
        },
        {
            'Endpoint': '/workouts/id',
            'method': 'GET',
            'body': None,
            'description': 'Return a workout'
        }
    ]

    return Response(routes)

## GET ALL EXERCISES ##
@api_view(['GET'])
def getExercices(request):
    exercises = Exercise.objects.all()

    serializer = ExerciseSerializer(exercises, many=True)

    return Response(serializer.data)

## GET AN EXERCISE ##
@api_view(['GET'])
def getExercice(request, pk):
    exercise = Exercise.objects.get(id=pk)

    serializer = ExerciseSerializer(exercise, many=False)

    return Response(serializer.data)

## POST AN EXERCISE
@api_view(['POST'])
def createExercise(request):

    data = request.data

    exercise = Exercise.objects.create(
        name = data['name'],
        bodyPart = data['bodyPart']
    )
    
    serializer = ExerciseSerializer(exercise, many=False)

    return Response(serializer.data)