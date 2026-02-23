cat > travel_information_system/urls.py <<'EOF'
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # homepage -> destinations
    path("", include("destinations.urls")),

    # accounts stays here
    path("accounts/", include("accounts.urls")),
]
EOF