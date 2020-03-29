import uuid

from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True, help_text='Creation date & time.')
    content = models.TextField()
