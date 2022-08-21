from django.urls import path

from . import views

urlpatterns = [
    path("orderoffers/", views.GetOrderOffersView.as_view(),
         name="orderoffer-list"),
    path("orderoffers/create/", views.CreateOrderOfferView.as_view(),
         name="orderoffer-create"),
    path("orderoffer/<int:pk>/", views.GetOrderOfferView.as_view(),
         name="orderoffer-detail"),
]
