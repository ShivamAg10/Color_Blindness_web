from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import UserAnswer, QuizResult

# Create your views here.

@login_required(login_url="/Accounts/Login")
def test(request):
    return render(request, "Blindness_Test/test.html")

@csrf_exempt  # for now, to allow JS POST; ideally use CSRF token later
@login_required(login_url="/Accounts/Login")
def quiz(request):
    if request.method == "POST":
        data = json.loads(request.body)
        answers = data.get("answers", [])
        score = 0
        total = len(answers)

        # Create QuizResult first (score will be updated after counting)
        quiz_result = QuizResult.objects.create(
            user=request.user,
            score=0,
            total_questions=total,
            result_type="Pending"
        )

        # Process answers
        for ans in answers:
            question = ans.get("question", "")
            selected = ans.get("selected", "")
            correct = ans.get("correct", "")

            is_correct = (selected == correct)
            if is_correct:
                score += 1

            UserAnswer.objects.create(
                user=request.user,
                question_text=question,
                selected_answer=selected,
                correct_answer=correct,
                is_correct=is_correct,
                quiz_result=quiz_result
            )

        # Determine blindness type (basic logic — you can expand)
        if score == total:
            result_type = "Normal Vision"
        elif score >= total * 0.6:
            result_type = "Mild Color Blindness"
        else:
            result_type = "Possible Color Blindness"

        # Update result
        quiz_result.score = score
        quiz_result.result_type = result_type
        quiz_result.save()

        return JsonResponse({
            "message": "Quiz submitted successfully",
            "score": score,
            "result_type": result_type
        })

    return render(request, "Blindness_Test/quiz.html")