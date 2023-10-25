from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

def home(request):
    return HttpResponse("success")


class UserView(APIView):
    def get(self, request):
        return Response("api01 success")
