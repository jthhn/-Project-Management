from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAdminOrProjectManager

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrProjectManager]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
