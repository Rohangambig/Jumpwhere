from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password, check_password
from .models import useModel ,Todo
from django.contrib.sessions.models import Session
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

from django.contrib.sessions.models import Session
from django.utils.timezone import now
from django.http import JsonResponse
import jwt
from django.conf import settings

def get_user_data(request):
    token = request.COOKIES.get('authToken')  # Get token from cookies

    if token:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_email = payload.get('email')

            user = useModel.objects.filter(email=user_email).first()
            if user:
                todos = Todo.objects.filter(user=user).values("title", "completed")

                return JsonResponse({
                    'username': user.name,
                    'email': user.email,
                    'todos': list(todos)
                })
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

    return JsonResponse({'error': 'User not authenticated'}, status=401)

    


def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def homePage(request):
    return render(request, 'home.html')

@csrf_exempt
def Register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            password = data.get('password')

            if not name or not email or not password:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            hashed_password = make_password(password)

            user = useModel(name=name, email=email, password=hashed_password)
            user.save()

            return JsonResponse({'message': 'User registered successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

import jwt
import datetime
from django.conf import settings

SECRET_KEY = "django-insecure-cy91hc72sn++^ie0otaa-fsx^tfql(cxil$*_yg6p_mbz$k5mw" 

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'error': 'Email and password required'}, status=400)

            user = useModel.objects.filter(email=email).first()
            if user and check_password(password, user.password):
                payload = {
                    'email': user.email,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                    'iat': datetime.datetime.utcnow()
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

                return JsonResponse({'message': 'Logged in', 'token': token}, status=200)

            return JsonResponse({"error": "Invalid credentials"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
