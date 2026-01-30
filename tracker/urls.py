from django.urls import path
from . import views
from .views_feedback import submit_feedback
from .views_feedback import feedback_dashboard

urlpatterns = [
    # Homepage
    path("", views.HomeView.as_view(), name="home"),

    # Authentication
    path("register/", views.register, name="register"),

    # Library Views
    path("library/", views.LibraryListView.as_view(), name="library_list"),
    path("library/add/", views.LibraryCreateView.as_view(), name="library_add"),
    path("library/<int:pk>/edit/", views.LibraryUpdateView.as_view(), name="library_edit"),
    path("library/<int:pk>/delete/", views.LibraryDeleteView.as_view(), name="library_delete"),
    path("submit-feedback/", submit_feedback, name="submit_feedback"),
    path("feedback-dashboard/", feedback_dashboard, name="feedback_dashboard"),
]