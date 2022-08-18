from django.urls import path

from . import views

urlpatterns = [
    path("orderoffers/", views.GetOrderOffersView.as_view(),
         name="orderoffers-list"),
    path("orderoffers/create/", views.CreateOrderOffersView.as_view(),
         name="orderoffers-create"),
    path("orderoffer/<int:pk>/", views.GetOrderOfferView.as_view(),
         name="orderoffers-detail"),
]
