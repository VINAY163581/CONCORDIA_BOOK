from django.urls import path
from . import views  # Corrected import statement

urlpatterns = [
    path('<str:course_code>/', views.display_textbooks, name='display_textbooks'),
]
