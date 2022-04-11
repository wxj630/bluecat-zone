from rest_framework import serializers

from service.models import Service
from user_info.serializers import UserDescSerializer



class ServiceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='service-detail')
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Service
        fields = '__all__'

class ServiceDetailSerializer(serializers.ModelSerializer):
    body_html = serializers.SerializerMethodField()
    toc_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Service
        fields = '__all__'


