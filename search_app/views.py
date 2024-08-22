from django.shortcuts import render
from .utilities import load_data
import os
from django.conf import settings
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')


def filter(request):
    data = []
    state_province = set()

    if request.method == 'POST':
        country = request.POST.get('country')
        data = load_data(country)

        file_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'world_universities_and_domains.json')

        with open(file_path, 'w') as file:
            json.dump(data, file)

        for item in data:
            if item['country'] == country and item['state-province']:
                state_province.add(item['state-province'])

    context = {
        'data': data,
        'state_province': state_province,
    }

    return render(request, 'home.html', context)
