from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api_assets.urls")),
    path("api/v1/", include("api_collections.urls")),
    path("api/v1/", include("api_contracts.urls")),
    path("api/v1/", include("api_users.urls")),
    path("api/v1/", include("api_transactions.urls")),
    path("api/v1/", include("api_events.urls")),
    path("api/v1/", include("api_tokens.urls")),
    path("api/v1/", include("api_orders.urls")),
    path("api/v1/", include("api_orderparameters.urls")),
    path("api/v1/", include("api_orderoffers.urls")),
    path("api/v1/", include("api_orderconsiderations.urls"))
]
