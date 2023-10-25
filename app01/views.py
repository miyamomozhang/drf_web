# from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.

def auth(request):
    return JsonResponse({"status": True, "message": "success"})


@api_view(['GET'])
def login(request):
    return Response({"status": True, "message": "success"})


# Django 的 CBV写法, from django.views import View
class UserView(View):
    def get(self, request):
        return JsonResponse({"CBV": "django"})


# Django restframework 的 CBV写法，from rest_framework.views import APIView
class InfoView(APIView):
    def get(self, request):
        return Response({"CBV": "django restframework"})
