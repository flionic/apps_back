from django.urls import path

from regions import views

urlpatterns = [
    path('', views.index, name='index'),
]
