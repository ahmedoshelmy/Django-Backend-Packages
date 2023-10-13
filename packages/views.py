from rest_framework import generics
from .models import Package
from .serializers import PackageSerializer


class PackageListView(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.order_by('price')

        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)

        return queryset
