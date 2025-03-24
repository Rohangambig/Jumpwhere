from django.utils.deprecation import MiddlewareMixin
import jwt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from .models import useModel

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get('Authorization')
        print("token",token)
        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                request.user = useModel.objects.get(email=payload['email'])
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, useModel.DoesNotExist):
                request.user = AnonymousUser()
        else:
            request.user = AnonymousUser()
