import requests
from django.shortcuts import render

def item_list_view(request):
    user_api_key = ''
    user_secret_key = ''

    headers = {
        'Authorization': f'token {user_api_key}:{user_secret_key}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    url = ''

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
    except Exception as e:
        data = None
        print(f"Error fetching data: {e}")

    return render(request, 'item_list.html', {'data': data['data']})
