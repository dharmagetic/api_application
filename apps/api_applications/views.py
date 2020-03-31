from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.api_applications.models import APIApplication
from apps.api_applications.serializers import APIApplicationCreateUpdateSerializer, APIApplicationDetailSerializer, \
    APIApplicationResetKeySerializer


class APIApplicationViewSet(ModelViewSet):
    queryset = APIApplication.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ['create', 'update', 'partial_update']:
            return APIApplicationCreateUpdateSerializer

        if self.action in ['list', 'retrieve']:
            return APIApplicationDetailSerializer


class APIApplicationResetKeyView(CreateAPIView):
    queryset = APIApplication.objects.all()
    serializer_class = APIApplicationResetKeySerializer

    lookup_field = 'id'
    lookup_url_kwarg = 'pk'

    def create(self, request, *args, **kwargs):
        api_application = self.get_object()

        api_application.reset_key()

        serializer = APIApplicationDetailSerializer(instance=api_application)
        return Response(serializer.data)


class APIApplicationTestDetailView(RetrieveAPIView):
    queryset = APIApplication.objects.all()
    serializer_class = APIApplicationDetailSerializer

    lookup_field = 'key'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        key = self.request.META.get('HTTP_API_APPLICATION_KEY', '')
        filter_kwargs = {self.lookup_field: key}
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj