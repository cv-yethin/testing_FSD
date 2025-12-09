from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[("lost", "Lost"), ("found", "Found")], default="lost")
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")