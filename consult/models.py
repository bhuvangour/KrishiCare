# models.py
from django.db import models

class Message(models.Model):
    user_message = models.TextField()
    bot_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_message}"