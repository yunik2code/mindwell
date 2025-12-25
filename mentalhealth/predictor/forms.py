# predictor/forms.py
from django import forms

class MentalHealthForm(forms.Form):
    age = forms.IntegerField(min_value=10, max_value=100)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-binary', 'Non-binary'), ('Other', 'Other')])
    employment_status = forms.ChoiceField(choices=[
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Student', 'Student'),
        ('Retired', 'Retired'),
        ('Self-employed', 'Self-employed')
    ])
    work_environment = forms.ChoiceField(choices=[('On-site', 'On-site'), ('Remote', 'Remote'), ('Hybrid', 'Hybrid')])
    mental_health_history = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    seeks_treatment = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    stress_level = forms.IntegerField(min_value=0, max_value=10, label="Stress Level (1–10)")
    sleep_hours = forms.FloatField(min_value=0, max_value=24)
    physical_activity_days = forms.IntegerField(min_value=0, max_value=7, label="Physical Activity Days (per week)")
    depression_score = forms.IntegerField(min_value=0, max_value=30)
    anxiety_score = forms.IntegerField(min_value=0, max_value=21)
    social_support_score = forms.IntegerField(min_value=0, max_value=100)
    productivity_score = forms.FloatField(min_value=0, max_value=100)