from django.urls import path

from . import views

urlpatterns = [
    path("contracts/", views.GetContractsView.as_view(), name="contract-list"),
    path("contract/<int:pk>/", views.GetContractView.as_view(),
         name="contract-detail"),
]
