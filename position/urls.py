from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from employee.urls import router as employee_router
router = DefaultRouter()

router.registry.extend(employee_router.registry)
app_name='check'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
