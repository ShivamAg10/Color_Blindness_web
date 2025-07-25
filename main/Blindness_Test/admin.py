from django.contrib import admin
from .models import QuizResult, UserAnswer

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'total_questions', 'result_type', 'submitted_at')
    list_filter = ('result_type', 'submitted_at')
    search_fields = ('user__username', 'result_type')

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question_text', 'selected_answer', 'correct_answer', 'is_correct')
    search_fields = ('user__username', 'question_text')
