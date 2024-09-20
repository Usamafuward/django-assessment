from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)


class Class(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    full_name = models.CharField(max_length=255)


class AssessmentArea(models.Model):
    name = models.TextField(max_length=255)


class Answer(models.Model):
    answer = models.CharField(max_length=50)


class Award(models.Model):
    name = models.CharField(max_length=255)


class Subject(models.Model):
    name = models.CharField(max_length=255)
    subject_score = models.DecimalField(max_digits=5, decimal_places=2)


class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.IntegerField()
    sydney_percentile = models.DecimalField(max_digits=5, decimal_places=2)
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.DecimalField(
        max_digits=5, decimal_places=2
    )
    correct_answer = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.IntegerField()
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=100)
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name="summary_answer"
    )
    # correct_answer = models.ForeignKey(
    #     Answer, on_delete=models.CASCADE, related_name="summary_correct_answer"
    # )
