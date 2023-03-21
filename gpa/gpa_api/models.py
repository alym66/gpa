from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


# class Subject(models.Model):
#     name = models.CharField(max_length=50)
#     subject_category = models.ForeignKey(
#         SubjectCategory,
#         related_name='subjects',
#         on_delete=models.CASCADE
#     )
#
#     class Meta:
#         ordering = ('name',)
#
#     def __str__(self):
#         return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    class Meta:
        ordering = ('name', 'surname',)

    def __str__(self):
        return self.name


class GPA(models.Model):
    student = models.ForeignKey(
        Student,
        related_name='gpa_score',
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    gpa = models.IntegerField()

    class Meta:
        ordering = ('gpa',)