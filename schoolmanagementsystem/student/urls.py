from django.urls import path

from schoolmanagementsystem.student import views

urlpatterns = [
    path("", views.student, name="student"),
]