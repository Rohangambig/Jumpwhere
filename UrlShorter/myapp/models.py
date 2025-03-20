from django.db import models
import random,string 

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters +  string.digits,k=6))

class shortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10,unique=True,default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"