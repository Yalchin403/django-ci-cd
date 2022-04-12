from django.urls import path
from .views import hello


app_name = 'core'

urlpatterns = [
    path('', hello, name="hello"),
]
