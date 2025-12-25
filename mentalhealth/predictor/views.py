# predictor/views.py
import joblib
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MentalHealthForm
from .models import MentalHealthRecord
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import pandas as pd
# from django.shortcuts import render, redirect

# Load model once at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model_files', 'mental_health_model.pkl')
PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), 'model_files', 'preprocessor.pkl')

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

@login_required
def predict_view(request):
    if request.method == 'POST':
        form = MentalHealthForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Define feature order (must match training)
            feature_names = [
                'age', 'gender', 'employment_status', 'work_environment',
                'mental_health_history', 'seeks_treatment', 'stress_level',
                'sleep_hours', 'physical_activity_days', 'depression_score',
                'anxiety_score', 'social_support_score', 'productivity_score'
            ]

            # Convert to DataFrame so ColumnTransformer can use column names
            input_df = pd.DataFrame([data], columns=feature_names)

            # Preprocess and predict
            input_processed = preprocessor.transform(input_df)
            prediction = model.predict(input_processed)[0]

            # Save to DB
            record = MentalHealthRecord(
                user=request.user,
                **data,
                predicted_risk=prediction
            )
            record.save()

            return render(request, 'predictor/result.html', {'risk': prediction, 'record': record})
    else:
        form = MentalHealthForm()
    return render(request, 'predictor/form.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'predictor/signup.html', {'form': form})

@login_required
def history_view(request):
    records = MentalHealthRecord.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'predictor/history.html', {'records': records})