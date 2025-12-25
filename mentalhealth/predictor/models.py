# predictor/models.py
from django.db import models
from django.contrib.auth.models import User

class MentalHealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    employment_status = models.CharField(max_length=50)
    work_environment = models.CharField(max_length=20)
    mental_health_history = models.CharField(max_length=10)  # Yes/No
    seeks_treatment = models.CharField(max_length=10)        # Yes/No
    stress_level = models.IntegerField()
    sleep_hours = models.FloatField()
    physical_activity_days = models.IntegerField()
    depression_score = models.IntegerField()
    anxiety_score = models.IntegerField()
    social_support_score = models.IntegerField()
    productivity_score = models.FloatField()
    predicted_risk = models.CharField(max_length=10)  # Low/Medium/High
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_risk} - {self.submitted_at}"