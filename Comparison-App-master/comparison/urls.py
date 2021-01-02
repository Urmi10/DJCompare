from django.urls import path
from . import views

app_name = 'comparison'

urlpatterns = [
    path('', views.home, name='comparison'),
    path('compare', views.compare, name='compare'),
]