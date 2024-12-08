# theoremreach_service.py
import requests
from django.conf import settings

class TheoremReachService:
    BASE_URL = 'https://api.theoremreach.com/api/publishers/v1/'

    def __init__(self):
        self.api_key = settings.THEOREMREACH_API_KEY

    def get_user_details(self, user_id, user_ip):
        endpoint = f'{self.BASE_URL}user_details'
        params = {
            'api_key': self.api_key,
            'user_id': user_id,
            'ip': user_ip,
        }
        response = requests.get(endpoint, params=params)
        return response.json()
