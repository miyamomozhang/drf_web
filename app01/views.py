# from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

def auth(request):
    return JsonResponse({"status": True, "message": "success"})


@api_view(['GET'])
def login(request):
    return Response({"status": True, "message": "success"})
