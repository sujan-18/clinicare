from .serializers import DoctorSerializer
from rest_framework import viewsets
from .models import Doctor
from .permissions import IsAdminOrReadOnly
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminOrReadOnly]
        