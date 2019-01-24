from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Schedule

# Create your views here.

# schedules = [{"hr": 11, "mn": 10}, {"hr": 10, "mn": 10}, {"hr": 9, "mn": 10}]


def home(request):
    context = {"schedules": Schedule.objects.all()}
    print(context)
    return render(request, "nmc/home.html", context)


class ScheduleListView(ListView):
    model = Schedule
    template_name = "nmc/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "schedules"
    ordering = ["date_added"]


class ScheduleDetailView(DetailView):
    model = Schedule


class ScheduleCreateView(LoginRequiredMixin, CreateView):
    model = Schedule
    fields = ["hr", "mn"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.uid = self.request.user
        return super().form_valid(form)


class ScheduleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Schedule
    fields = ["hr", "mn"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.uid = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.uid:
            return True
        return False


class ScheduleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Schedule
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.uid:
            return True
        return False


def about(request):
    return render(request, "nmc/about.html", {"title": "About"})
