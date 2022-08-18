from django.urls import path

from . import views

urlpatterns = [
    path("orderconsiderations/", views.GetOrderConsiderationsView.as_view(),
         name="orderconsideration-list"),
    path("orderconsiderations/create/", views.CreateOrderConsiderationsView.as_view(),
         name="orderconsideration-create"),
    path("orderconsideration/<int:pk>/", views.GetOrderConsiderationView.as_view(),
         name="orderconsideration-detail"),
]
