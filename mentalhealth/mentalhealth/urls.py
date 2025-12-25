# mentalhealth/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from predictor import views as predictor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predictor_views.predict_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='predictor/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', predictor_views.signup, name='signup'),
    path('history/', predictor_views.history_view, name='history'),
]