from django.urls import path

from . import views

urlpatterns = [
    path("orderparameters/", views.GetOrderParametersView.as_view(),
         name="orderparameter-list"),
    path("orderparameters/create/", views.CreateOrderParameterView.as_view(),
         name="orderparameter-create"),
    path("orderparameter/<int:pk>/", views.GetOrderParameterView.as_view(),
         name="orderparameter-detail"),
]
