from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
    return render(request, 'index.html')

def getWord(request):
    if request.method == 'GET':
        word = request.GET.get('word', "").strip()
        print("Word received:", word)

        if not word:
            return JsonResponse({"error": "No word provided"}, status=400)

        api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            try:
                meaning = data[0]['meanings'][0]['definitions'][0]['definition']
            except (IndexError, KeyError):
                meaning = "Definition not available."

            return JsonResponse({'message': 'Data fetched successfully', 'word': word, 'definition': meaning}, status=200)
        else:
            return JsonResponse({"error": "Word not found"}, status=404)
