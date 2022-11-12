from django.shortcuts import render

from django.http import HttpResponse

from regions.ipapi import get_region
from regions.utils import get_client_ip


def index(request):
    client_ip = get_client_ip(request)
    client_region = get_region(client_ip)
    return HttpResponse(f"Hi, you are from {client_region}")
