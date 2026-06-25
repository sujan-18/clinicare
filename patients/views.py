from .models import Patient
from .serializers import PatientSerializer
from rest_framework import viewsets
from .permissions import IsAdminOrOwnProfile

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAdminOrOwnProfile]

    def get_queryset(self):
        user = self.request.user

        # Admin can access all patient records
        if user.is_staff:
            return Patient.objects.all()
        
        # Patients can only access their own record
        return Patient.objects.filter(user=user)
