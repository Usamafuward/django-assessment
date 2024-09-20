from django.shortcuts import render
from .models import (
    School,
    Class,
    Student,
    Summary,
    AssessmentArea,
    Answer,
    Award,
    Subject,
)


def school_list(request):
    schools = School.objects.all()
    return render(request, "school.html", {"schools": schools})


def class_list(request):
    classes = Class.objects.all()
    return render(request, "class.html", {"classes": classes})


def student_list(request):
    students = Student.objects.all()
    return render(request, "student.html", {"students": students})


def assessment_area_list(request):
    assessment_areas = AssessmentArea.objects.all()
    return render(
        request, "assessment_area.html", {"assessment_areas": assessment_areas}
    )


def answer_list(request):
    answers = Answer.objects.all()
    return render(request, "answer.html", {"answers": answers})


def award_list(request):
    awards = Award.objects.all()
    return render(request, "award.html", {"awards": awards})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, "subject.html", {"subjects": subjects})


def summary_list(request):
    summaries = Summary.objects.all()
    return render(request, "summary.html", {"summaries": summaries})
