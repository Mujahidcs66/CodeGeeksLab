from django.shortcuts import render
import requests

def get_weather(request):
    if request.method == "POST":
        city = request.POST["city"]
        url = 'https://weatherapi-com.p.rapidapi.com/current.json'
        
        params = {
            'q': city
        }
        
        headers = {
            'X-RapidAPI-Key': '0ef34c4a59mshbe2649ba33254abp1a32c9jsn28091977c1ff',
            'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com',
        }
        
        try:
            response = requests.get(url=url, params=params, headers=headers)
            response_data = response.json()
            
            context = {
                'data': response_data
            }
            
            return render(request, 'weather/index.html', context)
        except requests.RequestException as e:
            return render(request, 'weather/index.html', {'error': e.strerror})
        
    return render(request, 'weather/index.html')
