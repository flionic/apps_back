from django.urls import path

from regions import views

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy-policy.html', views.privacy_policy, name='privacy'),
    path('terms.html', views.terms, name='terms'),
    path('api/check-user', views.check_user, name='check_user'),
    path('api/get-verification-code', views.verification_code_get, name='verification_code_get'),
    path('api/check-verification-approve', views.verification_code_approve, name='verification_code_approve'),
]
