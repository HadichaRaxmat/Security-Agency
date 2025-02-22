from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserContactSerializer
from rest_framework.permissions import AllowAny
from django.views.generic import FormView
CustomUser = get_user_model()
from .models import (Header, Menu, Slider, About, ServiceHeader, Service, Client, Touch, Team, Guard, Info, ContactUs,
                     Subscribe, Footer, UserContact, HeaderTouch)
from .forms import UserContactForm



def home_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def service_view(request):
    return render(request, "service.html")

def guard_view(request):
    return render(request, "guard.html")


def contact_view(request):
    return render(request, 'contact.html')



class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = UserContactForm
    success_url = reverse_lazy("/")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ваше сообщение успешно отправлено!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка! Проверьте введённые данные.")
        return super().form_invalid(form)






# API

class UserContactListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех контактов",
        responses={200: UserContactSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        contacts = UserContact.objects.all()
        serializer = UserContactSerializer(contacts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый контакт",
        request_body=UserContactSerializer,
        responses={201: UserContactSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = UserContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserContactDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить контакт",
        request_body=UserContactSerializer,
        responses={200: UserContactSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            contact = UserContact.objects.get(id=kwargs['pk'])
        except UserContact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частично обновить контакт",
        request_body=UserContactSerializer,
        responses={200: UserContactSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            contact = UserContact.objects.get(id=kwargs['pk'])
        except UserContact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить контакт",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            contact = UserContact.objects.get(id=kwargs['pk'])
        except UserContact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import HeaderSerializer


class HeaderListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех Header",
        responses={200: HeaderSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        headers = Header.objects.all()
        serializer = HeaderSerializer(headers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый Header",
        request_body=HeaderSerializer,
        responses={201: HeaderSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = HeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeaderDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить Header",
        request_body=HeaderSerializer,
        responses={200: HeaderSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderSerializer(header, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частично обновить Header",
        request_body=HeaderSerializer,
        responses={200: HeaderSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderSerializer(header, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить Header",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        header.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import MenuSerializer


class MenuListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех меню",
        responses={200: MenuSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый пункт меню",
        request_body=MenuSerializer,
        responses={201: MenuSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить пункт меню",
        request_body=MenuSerializer,
        responses={200: MenuSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частично обновить пункт меню",
        request_body=MenuSerializer,
        responses={200: MenuSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить пункт меню",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import SliderSerializer


class SliderListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all sliders",
        responses={200: SliderSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new slider",
        request_body=SliderSerializer,
        responses={201: SliderSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SliderDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a slider",
        request_body=SliderSerializer,
        responses={200: SliderSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            slider = Slider.objects.get(id=kwargs['pk'])
        except Slider.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SliderSerializer(slider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a slider",
        request_body=SliderSerializer,
        responses={200: SliderSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            slider = Slider.objects.get(id=kwargs['pk'])
        except Slider.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SliderSerializer(slider, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a slider",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            slider = Slider.objects.get(id=kwargs['pk'])
        except Slider.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        slider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import AboutSerializer


class AboutListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all About entries",
        responses={200: AboutSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        abouts = About.objects.all()
        serializer = AboutSerializer(abouts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new About entry",
        request_body=AboutSerializer,
        responses={201: AboutSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update an About entry",
        request_body=AboutSerializer,
        responses={200: AboutSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an About entry",
        request_body=AboutSerializer,
        responses={200: AboutSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an About entry",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        about.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import ServiceHeaderSerializer


class ServiceHeaderListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Service Headers",
        responses={200: ServiceHeaderSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        headers = ServiceHeader.objects.all()
        serializer = ServiceHeaderSerializer(headers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Service Header",
        request_body=ServiceHeaderSerializer,
        responses={201: ServiceHeaderSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = ServiceHeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceHeaderDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Service Header",
        request_body=ServiceHeaderSerializer,
        responses={200: ServiceHeaderSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            header = ServiceHeader.objects.get(id=kwargs['pk'])
        except ServiceHeader.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceHeaderSerializer(header, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Service Header",
        request_body=ServiceHeaderSerializer,
        responses={200: ServiceHeaderSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            header = ServiceHeader.objects.get(id=kwargs['pk'])
        except ServiceHeader.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceHeaderSerializer(header, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Service Header",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            header = ServiceHeader.objects.get(id=kwargs['pk'])
        except ServiceHeader.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        header.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import ServiceSerializer


class ServiceListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Services",
        responses={200: ServiceSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Service",
        request_body=ServiceSerializer,
        responses={201: ServiceSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Service",
        request_body=ServiceSerializer,
        responses={200: ServiceSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            service = Service.objects.get(id=kwargs['pk'])
        except Service.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Service",
        request_body=ServiceSerializer,
        responses={200: ServiceSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            service = Service.objects.get(id=kwargs['pk'])
        except Service.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Service",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            service = Service.objects.get(id=kwargs['pk'])
        except Service.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import ClientSerializer


class ClientListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Clients",
        responses={200: ClientSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Client",
        request_body=ClientSerializer,
        responses={201: ClientSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Client",
        request_body=ClientSerializer,
        responses={200: ClientSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(id=kwargs['pk'])
        except Client.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Client",
        request_body=ClientSerializer,
        responses={200: ClientSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(id=kwargs['pk'])
        except Client.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Client",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(id=kwargs['pk'])
        except Client.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import TouchSerializer


class TouchListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Touch items",
        responses={200: TouchSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        touches = Touch.objects.all()
        serializer = TouchSerializer(touches, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Touch item",
        request_body=TouchSerializer,
        responses={201: TouchSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = TouchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TouchDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Touch item",
        request_body=TouchSerializer,
        responses={200: TouchSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TouchSerializer(touch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Touch item",
        request_body=TouchSerializer,
        responses={200: TouchSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TouchSerializer(touch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Touch item",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        touch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import TeamSerializer


class TeamListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Team members",
        responses={200: TeamSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Team member",
        request_body=TeamSerializer,
        responses={201: TeamSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Team member",
        request_body=TeamSerializer,
        responses={200: TeamSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            team = Team.objects.get(id=kwargs['pk'])
        except Team.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Team member",
        request_body=TeamSerializer,
        responses={200: TeamSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            team = Team.objects.get(id=kwargs['pk'])
        except Team.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamSerializer(team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Team member",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            team = Team.objects.get(id=kwargs['pk'])
        except Team.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import GuardSerializer


class GuardListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all guards",
        responses={200: GuardSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        guards = Guard.objects.all()
        serializer = GuardSerializer(guards, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new guard",
        request_body=GuardSerializer,
        responses={201: GuardSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = GuardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuardDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a guard",
        request_body=GuardSerializer,
        responses={200: GuardSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            guard = Guard.objects.get(id=kwargs['pk'])
        except Guard.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GuardSerializer(guard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a guard",
        request_body=GuardSerializer,
        responses={200: GuardSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            guard = Guard.objects.get(id=kwargs['pk'])
        except Guard.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GuardSerializer(guard, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a guard",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            guard = Guard.objects.get(id=kwargs['pk'])
        except Guard.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        guard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import InfoSerializer


class InfoListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all info records",
        responses={200: InfoSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        info_list = Info.objects.all()
        serializer = InfoSerializer(info_list, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new info record",
        request_body=InfoSerializer,
        responses={201: InfoSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfoDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update an info record",
        request_body=InfoSerializer,
        responses={200: InfoSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            info = Info.objects.get(id=kwargs['pk'])
        except Info.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an info record",
        request_body=InfoSerializer,
        responses={200: InfoSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            info = Info.objects.get(id=kwargs['pk'])
        except Info.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InfoSerializer(info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an info record",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            info = Info.objects.get(id=kwargs['pk'])
        except Info.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import ContactUsSerializer


class ContactUsListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all ContactUs records",
        responses={200: ContactUsSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        contacts = ContactUs.objects.all()
        serializer = ContactUsSerializer(contacts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new ContactUs record",
        request_body=ContactUsSerializer,
        responses={201: ContactUsSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactUsDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a ContactUs record",
        request_body=ContactUsSerializer,
        responses={200: ContactUsSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            contact = ContactUs.objects.get(id=kwargs['pk'])
        except ContactUs.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactUsSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a ContactUs record",
        request_body=ContactUsSerializer,
        responses={200: ContactUsSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            contact = ContactUs.objects.get(id=kwargs['pk'])
        except ContactUs.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactUsSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a ContactUs record",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            contact = ContactUs.objects.get(id=kwargs['pk'])
        except ContactUs.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import SubscribeSerializer


class SubscribeListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Subscribe records",
        responses={200: SubscribeSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        subscriptions = Subscribe.objects.all()
        serializer = SubscribeSerializer(subscriptions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Subscribe record",
        request_body=SubscribeSerializer,
        responses={201: SubscribeSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscribeDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Subscribe record",
        request_body=SubscribeSerializer,
        responses={200: SubscribeSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            subscription = Subscribe.objects.get(id=kwargs['pk'])
        except Subscribe.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubscribeSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Subscribe record",
        request_body=SubscribeSerializer,
        responses={200: SubscribeSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            subscription = Subscribe.objects.get(id=kwargs['pk'])
        except Subscribe.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubscribeSerializer(subscription, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Subscribe record",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            subscription = Subscribe.objects.get(id=kwargs['pk'])
        except Subscribe.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import FooterSerializer


class FooterListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Footer records",
        responses={200: FooterSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        footers = Footer.objects.all()
        serializer = FooterSerializer(footers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Footer record",
        request_body=FooterSerializer,
        responses={201: FooterSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = FooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FooterDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Footer record",
        request_body=FooterSerializer,
        responses={200: FooterSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            footer = Footer.objects.get(id=kwargs['pk'])
        except Footer.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FooterSerializer(footer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Footer record",
        request_body=FooterSerializer,
        responses={200: FooterSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            footer = Footer.objects.get(id=kwargs['pk'])
        except Footer.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FooterSerializer(footer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Footer record",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            footer = Footer.objects.get(id=kwargs['pk'])
        except Footer.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        footer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import HeaderTouchSerializer


class HeaderTouchListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех HeaderTouch",
        responses={200: HeaderTouchSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        touches = HeaderTouch.objects.all()
        serializer = HeaderTouchSerializer(touches, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый HeaderTouch",
        request_body=HeaderTouchSerializer,
        responses={201: HeaderTouchSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = HeaderTouchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeaderTouchDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить HeaderTouch",
        request_body=HeaderTouchSerializer,
        responses={200: HeaderTouchSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            touch = HeaderTouch.objects.get(id=kwargs['pk'])
        except HeaderTouch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderTouchSerializer(touch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частично обновить HeaderTouch",
        request_body=HeaderTouchSerializer,
        responses={200: HeaderTouchSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            touch = HeaderTouch.objects.get(id=kwargs['pk'])
        except HeaderTouch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderTouchSerializer(touch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить HeaderTouch",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            touch = HeaderTouch.objects.get(id=kwargs['pk'])
        except HeaderTouch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        touch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
