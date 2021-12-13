from django.utils.decorators import method_decorator
from rest_framework import routers
from django.urls import path

from . import views

app_name = "api"

# router_v1 = routers.DefaultRouter()

# router_v1.register(r"v1/pets", views.PetViewSet, basename="pets")

# urlpatterns = router_v1.urls

# from django.views.generic import TemplateView
# from django.conf import settings

urlpatterns = [
    path('v1/pets/', views.OrderListDeleteView.as_view(), ),
]