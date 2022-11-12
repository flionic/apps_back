from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect

from regions.ipapi import get_region
from regions.utils import get_client_ip
from regions.models import LinksList


def index(request):
    client_ip = get_client_ip(request)
    client_country = get_region(client_ip)

    region_links = LinksList.objects.filter(country=client_country).first()

    if region_links:
        return redirect(region_links.url)

    return HttpResponse(f"Default Landing ({client_country})")
