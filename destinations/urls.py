cat > destinations/urls.py <<'EOF'
from django.urls import path
from . import views

urlpatterns = [
    path("", views.travel_home, name="travel_home"),
]
EOF