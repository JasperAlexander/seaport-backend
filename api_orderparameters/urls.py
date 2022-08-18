from django.urls import path

from . import views

urlpatterns = [
    path("orderparameters/", views.GetOrderParametersView.as_view(),
         name="orderparameters-list"),
    path("orderparameters/create/", views.CreateOrderParametersView.as_view(),
         name="orderparameters-create"),
    path("orderparameter/<int:pk>/", views.GetOrderParameterView.as_view(),
         name="orderparameters-detail"),
]
