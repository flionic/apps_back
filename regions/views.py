import random

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from regions.ipapi import get_region
from regions.utils import get_client_ip
from regions.models import LinksList


def index(request):
    client_ip = get_client_ip(request)
    client_country = get_region(client_ip)

    region_link = LinksList.objects.filter(country=client_country).first()

    if region_link:
        region_link.counter += 1
        region_link.save()
        return redirect(region_link.url)

    template = loader.get_template('index.html')
    context = {"country": client_country}
    return HttpResponse(template.render(context))


def privacy_policy(request):
    template = loader.get_template('privacy-policy.html')
    return HttpResponse(template.render())


def terms(request):
    template = loader.get_template('terms.html')
    return HttpResponse(template.render())


# class CheckUserAPIView(APIView):
#     """
#     must be have: app_id, location_phone, location_facebook, user_lang, test_mode
#     """
#     # @staticmethod
#     def post(self, request):
#         if 'app_id' in request.data:
#             if request.data["app_id"] == "dating_artma":
#                 if ('test_mode' in request.data) and 'test_mode' == 1:
#                     return JsonResponse(
#                         {
#                             'grant_access': 1,
#                             'webview_url': 'https://s-appteam.com/',
#                             'final_url': 'https://s-appteam.com/my-account/',
#                         }
#                     )
#
#         return JsonResponse(
#             {
#                 'grant_access': 0,
#             }
#         )

@csrf_exempt
@api_view(['POST'])
def check_user(request):
    """
    must be have: app_id, location_phone, location_facebook, user_lang, test_mode
    """
    if 'app_id' in request.data:
        # client_ip = get_client_ip(request)
        # print(client_ip)
        if request.data['app_id'] == 'dating_artma1':
            if ('test_mode' in request.data) and ((request.data['test_mode'] is True) or request.data['test_mode'] == 1):
                return Response(
                    {
                        'grant_access': True,
                        'webview_url': 'https://s-appteam.com/',
                        'final_urls': [
                            'https://s-appteam.com/my-account/',
                            'https://s-appteam.com/shop/'
                        ],
                    },
                    status=status.HTTP_200_OK
                )

    return Response(
        {
            'grant_access': False,
        },
        status=status.HTTP_403_FORBIDDEN
    )


@csrf_exempt
@api_view(['POST'])
def verification_code_get(request):
    if 'app_id' in request.data and 'phone_number' in request.data and request.data['phone_number'] != '+111':
        if request.data['app_id'] == 'gameslist_apl':
            # save request.data['phone_number']
            return Response(
                {
                    'success': True,
                    'otp_code': random.randint(100000, 999999),
                },
                status=status.HTTP_200_OK
            )

    return Response(
        {
            'success': False,
        },
        status=status.HTTP_403_FORBIDDEN
    )


@csrf_exempt
@api_view(['POST'])
def verification_code_approve(request):
    if 'app_id' in request.data:
        if request.data['app_id'] == 'gameslist_apl':
            # save request.data['phone_number']
            if 'phone_number' in request.data and 'otp_code' in request.data:
                if request.data['phone_number'] == '+111' and request.data['otp_code'] == '111111':
                    return Response(
                        {
                            'success': True,
                        },
                        status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {
                            'success': False,
                            'error_message': "OTP code doesn't match",
                        },
                        status=status.HTTP_200_OK
                    )

    return Response(
        {
            'success': False,
        },
        status=status.HTTP_403_FORBIDDEN
    )
