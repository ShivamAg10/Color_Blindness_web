from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserAnswer, QuizResult
from collections import defaultdict
import json


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

        category_scores = defaultdict(lambda: {"correct": 0, "total": 0})

        # Process answers
        for ans in answers:
            question = ans.get("question", "")
            selected = ans.get("selected", "")
            correct = ans.get("correct", "")
            category = ans.get("category", "unknown")

            is_correct = (selected == correct)
            if is_correct:
                score += 1
                category_scores[category]["correct"] += 1
            category_scores[category]["total"] += 1

            UserAnswer.objects.create(
                user=request.user,
                question_text=question,
                selected_answer=selected,
                correct_answer=correct,
                is_correct=is_correct,
                quiz_result=quiz_result
            )

        # Determine blindness type (basic logic — you can expand)
        result_type = "normal Vision"
        notes = []
        
        for cat, stats in category_scores.items():
            accuracy = stats["correct"] / stats["total"] if stats['total'] else 0
            
            if cat == "red-green" and accuracy < 0.6:
                result_type = "Red-Green Color Blindness"
                notes.append("Low accuracy in red-green discrimination.")
            elif cat == "blue-yellow" and accuracy < 0.6:
                result_type = "Blue-Yellow Color Blindness"
                notes.append("Low accuracy in blue-yellow discrimination.")
            elif cat == "control" and accuracy < 0.5:
                result_type = "Possible Total Color Blindness"
                notes.append("Even control questions were often incorrect.")

        # Update result
        quiz_result.score = score
        quiz_result.result_type = result_type
        quiz_result.category_breakdown = category_scores
        quiz_result.save()

        return JsonResponse({
            "message": "Quiz submitted successfully",
            "score": score,
            "result_type": result_type,
            "details": category_scores,
            "notes": notes
        })

    return render(request, "Blindness_Test/quiz.html")