from django.shortcuts import render
import requests
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def weather_view(request):
    city=request.query_params.get('city','Delhi')#by default delhi will be displayed
    api_key='823a086df42534d65f52a2d5d979cea1'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        return JsonResponse({
            "city": data.get("name"),
            "temperature": data["main"].get("temp"),
            "weather":data["weather"][0].get("description"),
            "humidity": data["main"].get("humidity"),
            "wind_speed": data["wind"].get("speed"),
            "Feels_like": data["main"].get("feels_like")


        },status=status.HTTP_200_OK)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)





