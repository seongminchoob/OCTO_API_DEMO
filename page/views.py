import requests

from django.conf import settings
from django.shortcuts import render

# expired token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTc0OTMzMTksInR5cGUiOiJhY2Nlc3MiLCJ1aWQiOiJxU2tHMmhVTm1ZYWVkTmVERjZJelN5bHFoUlEyIn0.bnjoA2emq2iWn31kvxpkV_BTb05HC6OGMKsYt4ILSkE

def index(request):
    access_token = request.COOKIES.get('access-token')
    if not access_token:
        access_token = fetch_access_token(request)
    r = fetch_gym_data(access_token)
    if r.status_code == 401:
        access_token = fetch_access_token(request)
        r = fetch_gym_data(access_token)
    response = render(request, "page_template.html", {"gyms": r.json()})
    response.set_cookie("access-token", access_token, 3 * 24 * 60 * 60)
    return response


def fetch_gym_data(access_token):
    return requests.get(
            url="https://octo-api.asuc.org/gyms",
            headers={
                'Content-Type': 'application/json',
                'Authorization': "Bearer " + access_token
            })


def fetch_access_token(request):
    refresh_token = settings.REFRESH_TOKEN
    r = requests.post(url="https://octo-api.asuc.org/refresh-token",
                      headers={'Content-Type': 'application/json'},
                      json={
                          "refresh-token": refresh_token
                        }
                      )
    data = r.json()
    access_token = data["access-token"]
    return access_token