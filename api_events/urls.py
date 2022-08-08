from django.urls import path

from . import views

urlpatterns = [
    path("events/", views.GetEventsView.as_view(),
         name="event-list"),
    path("event/<int:pk>/", views.GetEventView.as_view(),
         name="event-detail"),
]
