from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    edition = models.CharField(max_length=100, blank=True, null=True)
    condition_choices = [
        ('new', 'New'),
        ('good', 'Good'),
        ('written', 'Written'),
        ('old', 'Old'),
    ]
    condition = models.CharField(max_length=20, choices=condition_choices)
    course_code = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.condition})"
