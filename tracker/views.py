from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Library

class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    template_name = "library_list.html"
    context_object_name = "libraries"

    def get_queryset(self):
        return Library.objects.filter(user=self.request.user)

class LibraryCreateView(LoginRequiredMixin, CreateView):
    model = Library
    fields = ["edition", "platform", "status", "priority", "hours_played", "notes"]
    template_name = "library_form.html"
    success_url = reverse_lazy("library_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LibraryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Library
    fields = ["edition", "platform", "status", "priority", "hours_played", "notes"]
    template_name = "library_form.html"
    success_url = reverse_lazy("library_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        library = self.get_object()
        return library.user == self.request.user

class LibraryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Library
    template_name = "library_confirm_delete.html"
    success_url = reverse_lazy("library_list")

    def test_func(self):
        library = self.get_object()
        return library.user == self.request.user