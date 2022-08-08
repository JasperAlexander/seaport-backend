from django.urls import path

from . import views

urlpatterns = [
    path("orders/", views.GetOrdersView.as_view(),
         name="order-list"),
    path("order/<int:pk>/", views.GetOrderView.as_view(),
         name="order-detail"),
]
