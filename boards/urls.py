from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexPageView.as_view(),name='index'),
]