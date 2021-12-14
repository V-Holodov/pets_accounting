from . import routers, views

app_name = "api"

router_v1 = routers.CustomBulkDeleteRouter()
router_v1.register("v1/pets", views.PetViewSet, basename="pets")

urlpatterns = router_v1.urls
