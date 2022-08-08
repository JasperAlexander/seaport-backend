from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.GetUsersView.as_view(), name="user-list"),
    path("user/<int:pk>/", views.GetUserView.as_view(),
         name="user-detail"),
]
