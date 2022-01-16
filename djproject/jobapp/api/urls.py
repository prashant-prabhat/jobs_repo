from django.urls import path,include
from jobapp import views
from jobapp.api.views import HydJobsCRUDCBV
from rest_framework import routers

router=routers.DefaultRouter()
router.register('hydjobsinfo',HydJobsCRUDCBV,basename='hydjobsinfo')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',include(router.urls))
]
