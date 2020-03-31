from rest_framework import serializers

from apps.api_applications.models import APIApplication


class APIApplicationCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIApplication
        fields = ('name',)


class APIApplicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIApplication
        fields = '__all__'


class APIApplicationResetKeySerializer(serializers.Serializer):
    pass
