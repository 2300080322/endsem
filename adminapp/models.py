from django.db import models
from trainerapp.models import Course, Trainer  # Replace 'trainerapp' with the correct app name

class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.course} by {self.trainer}"
