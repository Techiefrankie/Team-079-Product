"""View classes for reporter app."""
from rest_framework import generics
from reporter.models import IncidentReport
from reporter import serializers


# Create your views here.
class CreateIncidentReportView(generics.ListCreateAPIView):
    queryset = IncidentReport.objects.all()
    serializer_class = serializers.IncidentSerializer


class DetailIncidentReportView(generics.RetrieveUpdateAPIView):
    queryset = IncidentReport.objects.all()
    serializer_class = serializers.IncidentSerializer