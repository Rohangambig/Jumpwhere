from django.urls import path
from myapp.views import shorten_url, redirect_to_original

urlpatterns = [
    path("", shorten_url, name="shorten_url"),
    path("<str:short_code>/", redirect_to_original, name="redirect_to_original"),
]
