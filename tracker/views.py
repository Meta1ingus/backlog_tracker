from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Library, Platform, Status


class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    template_name = "library_list.html"
    context_object_name = "libraries"
    def get_paginate_by(self, queryset):
        page_size = self.request.GET.get("page_size")
        if page_size and page_size.isdigit():
            return int(page_size)
        return 20  # default

    def get_queryset(self):
        queryset = Library.objects.filter(user=self.request.user)

        # --- filtering ---
        platform = self.request.GET.get("platform")
        status = self.request.GET.get("status")
        priority = self.request.GET.get("priority")

        if platform:
            queryset = queryset.filter(platform__id=platform)

        if status:
            queryset = queryset.filter(status__id=status)

        if priority:
            queryset = queryset.filter(priority=priority)

        # --- search ---
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                edition__game__title__icontains=search
            )

        # --- sorting ---
        sort = self.request.GET.get("sort")

        if sort == "name":
            queryset = queryset.order_by(
                "edition__game__title"
            )

        elif sort == "name_desc":
            queryset = queryset.order_by(
                "-edition__game__title"
            )

        elif sort == "platform":
            queryset = queryset.order_by(
                "platform__name",
                "edition__game__title"
            )

        elif sort == "platform_desc":
            queryset = queryset.order_by(
                "-platform__name",
                "edition__game__title"
            )

        elif sort == "status":
            queryset = queryset.order_by(
                "status__order",
                "priority",
                "edition__game__title"
            )

        elif sort == "status_desc":
            queryset = queryset.order_by(
                "-status__order",
                "priority",
                "edition__game__title"
            )

        elif sort == "priority":
            queryset = queryset.order_by(
                "priority",
                "edition__game__title"
            )

        elif sort == "priority_desc":
            queryset = queryset.order_by(
                "-priority",
                "edition__game__title"
            )

        # --- Default multi-column sort ---
        else:
            queryset = queryset.order_by(
                "status__order",
                "priority",
                "edition__game__title"
            )

        return queryset

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # sorting
    context["current_sort"] = self.request.GET.get("sort", "")

    # filtering
    context["platforms"] = Platform.objects.all()
    context["statuses"] = Status.objects.all()
    context["priorities"] = range(1, 6)

    context["selected_platform"] = self.request.GET.get("platform", "")
    context["selected_status"] = self.request.GET.get("status", "")
    context["selected_priority"] = self.request.GET.get("priority", "")

    # --- pagination: preserve querystring ---
    params = self.request.GET.copy()
    if "page" in params:
        params.pop("page")

    context["preserved_querystring"] = "&" + params.urlencode() if params else ""

    return context

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