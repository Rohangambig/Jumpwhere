from django.http import HttpResponseRedirect, JsonResponse
import random
import string
from django.shortcuts import render

short_url_mapping = {}

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(request):
    if request.method == "POST":
        import json

        try:
            data = json.loads(request.body)
            original_url = data.get("original_url", "").strip()
            if not original_url:
                return JsonResponse({"error": "No URL provided"}, status=400)

            short_code = generate_short_code()
            short_url_mapping[short_code] = original_url  

            return JsonResponse({"short_url": f"http://127.0.0.1:8000/{short_code}"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return render(request, "home.html")

def redirect_to_original(request, short_code):
    original_url = short_url_mapping.get(short_code)
    if original_url:
        return HttpResponseRedirect(original_url)
    return JsonResponse({"error": "Shortened URL not found"}, status=404)
