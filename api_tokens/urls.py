from django.urls import path

from . import views

urlpatterns = [
    path("tokens/", views.GetTokensView.as_view(),
         name="token-list"),
    path("token/<int:pk>/", views.GetTokenView.as_view(),
         name="token-detail"),
]
