from django.urls import path
from . import views

urlpatterns = [
    path("", views.LibraryListView.as_view(), name="library_list"),
    path('library/', views.LibraryListView.as_view(), name='library_list'),
    path('library/add/', views.LibraryCreateView.as_view(), name='library_add'),
    path('library/<int:pk>/edit/', views.LibraryUpdateView.as_view(), name='library_edit'),
    path('library/<int:pk>/delete/', views.LibraryDeleteView.as_view(), name='library_delete'),
]
