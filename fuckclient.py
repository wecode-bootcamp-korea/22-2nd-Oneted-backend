from django.test import Client
import requests
headers = {
            'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo3fQ.e7ograiiZoyWre5mmRTZ4A_eqBNK14NIRAV4MY--V5Q', 
        }
response = requests.get("http://localhost:8000/resumes/20", headers=headers)
print(response)