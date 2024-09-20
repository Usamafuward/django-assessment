# your_app/management/commands/load_csv.py
import os
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from assessment.models import (
    School,
    Class,
    Student,
    AssessmentArea,
    Answer,
    Award,
    Subject,
    Summary,
)


class Command(BaseCommand):
    help = "Load data from CSV and populate models"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, "data/Ganison_dataset_1.csv")

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Get or create School
                school, _ = School.objects.get_or_create(name=row["school_name"])

                # Get or create Class
                student_class, _ = Class.objects.get_or_create(name=row["Class"])

                # Get or create Student
                full_name = f"{row['First Name']} {row['Last Name']}"
                student, _ = Student.objects.get_or_create(full_name=full_name)

                # Get or create Subject
                subject, _ = Subject.objects.get_or_create(
                    name=row["Subject"],
                    defaults={"subject_score": row["student_score"]},
                )

                # Get or create Assessment Area
                assessment_area, _ = AssessmentArea.objects.get_or_create(
                    name=row["Assessment Areas"]
                )

                # Get or create Answers for both answer and correct answer
                answer, _ = Answer.objects.get_or_create(answer=row["Answers"])
                correct_answer, _ = Answer.objects.get_or_create(
                    answer=row["Correct Answers"]
                )

                # Get or create Award
                award, _ = Award.objects.get_or_create(name=row["award"])

                # Create Summary entry
                Summary.objects.create(
                    school=school,
                    sydney_participant=row["sydney_participants"],
                    sydney_percentile=row["sydney_percentile"],
                    assessment_area=assessment_area,
                    award=award,
                    class_name=student_class,
                    correct_answer_percentage_per_class=row[
                        "correct_answer_percentage_per_class"
                    ],
                    correct_answer=correct_answer.answer,
                    student=student,
                    participant=row["participant"],
                    student_score=row["student_score"],
                    subject=subject,
                    category_id=row[
                        "Question Number"
                    ],  # Assuming category_id is related to question number
                    year_level_name=row["Year Level"],
                    answer=answer,
                    # correct_answer=correct_answer,
                )

        self.stdout.write(self.style.SUCCESS("Data successfully loaded into models"))
