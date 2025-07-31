from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=150, default="Unknown")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} at {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
