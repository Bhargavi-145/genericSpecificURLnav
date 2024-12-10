from django.urls import path
from zomato.views import *
app_name = 'zomato'

urlpatterns = [
    path('biriyani/', biriyani, name='biriyani')
]
