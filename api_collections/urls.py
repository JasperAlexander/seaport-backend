from django.urls import path

from . import views

urlpatterns = [
    path("collections/", views.GetCollectionsView.as_view(), name="collection-list"),
    path("collection/<str:slug>/", views.GetCollectionView.as_view(),
         name="collection-detail"),
]
