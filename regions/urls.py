from django.urls import path

from regions import views

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy-policy.html', views.privacy_policy, name='privacy'),
    path('terms.html', views.terms, name='terms'),
]
