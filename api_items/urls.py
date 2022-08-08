from django.urls import path

from . import views

urlpatterns = [
    path("items/", views.GetItemsView.as_view(),
         name="item-list"),
    path("item/<int:pk>/", views.GetItemView.as_view(),
         name="item-detail"),
]
