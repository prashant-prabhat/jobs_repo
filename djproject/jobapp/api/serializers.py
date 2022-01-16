from rest_framework.serializers import ModelSerializer
from jobapp.models import hydjobs
class HydJobsSerializer(ModelSerializer):
    class Meta:
        model=hydjobs
        fields='__all__'
