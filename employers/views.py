from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Employer
from .serializers import EmployerSerializer

class EmployerListCreateView(generics.ListCreateAPIView):
    """GET /api/employers/ (list) and POST /api/employers/ (create)"""
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return employers owned by the current user:contentReference[oaicite:26]{index=26}
        return Employer.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """GET/PUT/DELETE /api/employers/<id>/"""
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow access to the user's own employers:contentReference[oaicite:27]{index=27}
        return Employer.objects.filter(owner=self.request.user)
