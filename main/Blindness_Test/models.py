from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    result_type = models.CharField(max_length=100)  # e.g. 'Normal', 'Deuteranopia'
    submitted_at = models.DateTimeField(auto_now_add=True)
    category_breakdown = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username} - {self.result_type} ({self.score}/{self.total_questions})"

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    selected_answer = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    is_correct = models.BooleanField()
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"{self.user.username} - {self.question_text[:30]}..."
