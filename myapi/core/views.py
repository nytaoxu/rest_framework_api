from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
          'message': 'Hello, World!'
        }
        result = ""
        for attr, value in vars(request).items():
            result += str(attr) + ": " + str(value) + ". ----- "
        # return Response(result)
        return Response(content)
