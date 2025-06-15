from rest_framework import viewsets, generics, filters
from factory_app.models import Man, Method, Machine, Material
from .serializers import ManSerializer, MethodSerializer, MachineSerializer, MaterialSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ManViewSet(viewsets.ModelViewSet):
    queryset = Man.objects.all()
    serializer_class = ManSerializer

    @action(detail=True, methods=['get'])
    def methods(self, request, pk=None):
        man = self.get_object()
        methods = Method.objects.filter(responsible_man=man)
        serializer = MethodSerializer(methods, many=True)
        return Response(serializer.data)

class MethodViewSet(viewsets.ModelViewSet):
    queryset = Method.objects.all()
    serializer_class = MethodSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MethodListCreateAPIView(generics.ListCreateAPIView):
    queryset = Method.objects.all()
    serializer_class = MethodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'responsible_man__name']



