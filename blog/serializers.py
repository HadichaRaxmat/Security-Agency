from rest_framework import serializers
from .models import  (UserContact, Header, Menu, HeaderTouch, About, Slider, ServiceHeader, Service, Client, Touch, Team,
                      Guard, Info, ContactUs, Subscribe, Footer)

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    message = serializers.CharField(max_length=500)


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        read_only_fields = ('id' ,)
        fields =['id', 'name', 'email', 'phone', 'message']



class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        read_only_fields = ('id',)
        fields = ['id', 'logo']



class MenuSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        read_only_fields = ('id', 'url')
        fields = ['id', 'menu', 'title', 'is_active', 'url']

    def get_url(self, obj):
        return obj.get_url()



class HeaderTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderTouch
        read_only_fields = ('id',)
        fields = ['id', 'method']



class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        read_only_fields = ('id',)
        fields = ['id', 'image', 'title', 'title_continue', 'text', 'last']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        read_only_fields = ('id',)
        fields = ['id', 'image', 'title', 'text', 'last']



class ServiceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHeader
        read_only_fields = ('id',)
        fields = ['id', 'title']



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        read_only_fields = ('id',)
        fields = ['id', 'title', 'text', 'last']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = ('id',)
        fields = ['id', 'image', 'name', 'title', 'text']


class TouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Touch
        read_only_fields = ('id',)
        fields = ['id', 'image', 'title', 'last']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = ('id',)
        fields = ['id', 'title', 'text', 'last']


class GuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guard
        read_only_fields = ('id',)
        fields = ['id', 'name', 'status', 'image']



class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        read_only_fields = ('id',)
        fields = ['id', 'title', 'text']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        read_only_fields = ('id',)
        fields = ['id', 'title']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        read_only_fields = ('id',)
        fields = ['id', 'title', 'email', 'last']


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        read_only_fields = ('id',)
        fields = ['id', 'info']