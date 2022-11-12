from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from regions.ipapi import get_region
from regions.utils import get_client_ip
from regions.models import LinksList


def index(request):
    client_ip = get_client_ip(request)
    client_ip = '46.211.108.219'
    client_country = get_region(client_ip)

    region_link = LinksList.objects.filter(country=client_country).first()

    if region_link:
        region_link.counter += 1
        region_link.save()
        return redirect(region_link.url)

    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def privacy_policy(request):
    template = loader.get_template('privacy-policy.html')
    return HttpResponse(template.render())


def terms(request):
    template = loader.get_template('terms.html')
    return HttpResponse(template.render())
