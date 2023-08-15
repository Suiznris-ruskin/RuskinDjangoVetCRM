from django.apps import AppConfig
import requests
import boto3
from django.http import JsonResponse

class RuskinvetappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ruskinvetapp'



