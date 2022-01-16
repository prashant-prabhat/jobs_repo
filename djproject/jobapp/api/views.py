from rest_framework import viewsets
from jobapp.models import hydjobs
from jobapp.api.serializers import HydJobsSerializer
class HydJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class = HydJobsSerializer
    queryset=hydjobs.objects.all()
