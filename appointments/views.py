from .serializers import AppointmentSerializer
from rest_framework import viewsets
from .models import Appointment
from doctors.permissions import IsAdminOrReadOnly

class AppointmentViewSet(viewsets.ModelViewSet):
        queryset = Appointment.objects.all()
        serializer_class = AppointmentSerializer
        permission_classes = [IsAdminOrReadOnly]