from rest_framework.decorators import api_view
from rest_framework.response import Response

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