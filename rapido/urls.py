from django.urls import path
from rapido.views import *
app_name = 'rapido'

urlpatterns = [
    path('auto/', auto, name='auto')
]