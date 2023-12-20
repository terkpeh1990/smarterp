
from django.core.mail import send_mail
from .models import *
from company.models import Tenants
from authentication.models import User
from erpproject.settings import  endPoint,key,Sender_Id
import requests


def incrementor():
    info = {"count": 100}
    def number():
        info["count"] += 1
        return info["count"]
    return number





   