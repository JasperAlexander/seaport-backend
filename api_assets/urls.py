from django.urls import path

from . import views

urlpatterns = [
    path("assets/", views.GetAssetsView.as_view(), name="asset-list"),
    path("assets/create/", views.CreateAssetView.as_view(), name="asset-create"),
    path("asset/<str:asset_contract__address>/<str:token_id>/",
         views.GetAssetView.as_view(), name="asset-detail"),
    #     path("asset/<str:asset_contract__address>/<str:token_id>/destroy/",
    #          views.DestroyAssetView.as_view(), name="asset-destroy"),
    path("asset/<str:asset_contract__address>/<str:token_id>/update/",
         views.UpdateAssetView.as_view(), name="asset-update"),
]
