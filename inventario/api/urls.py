from rest_framework import routers
from inventario.api.views import ProductoViewSet
router = routers.DefaultRouter()
router.register('productos', ProductoViewSet, 'producto')
urlpatterns = router.urls