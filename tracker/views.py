from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Library

class LibraryListView(ListView):
    model = Library
    template_name = "library_list.html"
    context_object_name = "libraries"

class LibraryCreateView(CreateView):
    model = Library
    fields = ["edition", "platform", "status", "priority", "hours_played", "notes"]
    template_name = "library_form.html"
    success_url = reverse_lazy("library_list")

class LibraryUpdateView(UpdateView):
    model = Library
    fields = ["edition", "platform", "status", "priority", "hours_played", "notes"]
    template_name = "library_form.html"
    success_url = reverse_lazy("library_list")

class LibraryDeleteView(DeleteView):
    model = Library
    template_name = "library_confirm_delete.html"
    success_url = reverse_lazy("library_list")