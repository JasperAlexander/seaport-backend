from django.urls import path

from . import views

urlpatterns = [
    path("transactions/", views.GetTransactionsView.as_view(),
         name="transaction-list"),
    path("transaction/<int:pk>/", views.GetTransactionView.as_view(),
         name="transaction-detail"),
]
