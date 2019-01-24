from django.urls import path
from .views import (
    ScheduleListView,
    ScheduleDetailView,
    ScheduleCreateView,
    ScheduleUpdateView,
    ScheduleDeleteView,
)
from . import views

urlpatterns = [
    path("", ScheduleListView.as_view(), name="nmc-home"),
    path("schedule/<int:pk>/", ScheduleDetailView.as_view(), name="sch-detail"),
    path("schedule/new/", ScheduleCreateView.as_view(), name="sch-create"),
    path("schedule/<int:pk>/update", ScheduleUpdateView.as_view(), name="sch-update"),
    path("schedule/<int:pk>/delete", ScheduleDeleteView.as_view(), name="sch-delete"),
    path("about/", views.about, name="nmc-about"),
]

