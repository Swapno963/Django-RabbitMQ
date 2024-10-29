from django.shortcuts import render
from django.http import HttpResponse
from .rabbitmq import publish_message


def index(request):
    publish_message("Hi, This is swapno")
    return HttpResponse("message delevered to rebittmq")
