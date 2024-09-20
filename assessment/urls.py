from django.urls import path
from . import views

urlpatterns = [
    path("schools/", views.school_list, name="school_list"),
    path("classes/", views.class_list, name="class_list"),
    path("students/", views.student_list, name="student_list"),
    path("assessment-areas/", views.assessment_area_list, name="assessment_area_list"),
    path("answers/", views.answer_list, name="answer_list"),
    path("awards/", views.award_list, name="award_list"),
    path("subjects/", views.subject_list, name="subject_list"),
    path("summary/", views.summary_list, name="summary_list"),
]
