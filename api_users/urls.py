from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.GetUsersView.as_view(), name="user-list"),
    path("users/create/", views.CreateUserView.as_view(), name="user-create"),
    path("user/<str:username>/", views.GetUserView.as_view(),
         name="user-detail")
]
