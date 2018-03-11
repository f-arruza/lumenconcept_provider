from provider import urls

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import response, schemas
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes

from .utils import send_message_sqs
from .models import (Category, Requirement, Provider, Support, Calification)
from .serializers import (CategorySerializer, RequirementSerializer,
                          ProviderSerializer, SupportSerializer,
                          CalificationSerializer)

# Create your views here.
@api_view()
@permission_classes((AllowAny, ))
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='LumenConcept Provider API Docs',
                                        patterns=urls.api_url_patterns,
                                        url='/api/v1/')
    return response.Response(generator.get_schema())


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class RequirementViewSet(viewsets.ModelViewSet):
    serializer_class = RequirementSerializer
    queryset = Requirement.objects.all()


class SupportViewSet(viewsets.ModelViewSet):
    serializer_class = SupportSerializer
    queryset = Support.objects.all()


class CalificationViewSet(viewsets.ModelViewSet):
    serializer_class = CalificationSerializer
    queryset = Calification.objects.all()


class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    def create(self, request):
        serializer = ProviderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)

        provider = serializer.save()

        registry_detail = {
            "id": str(provider.id),
            "provider_code": str(provider.code),
            "provider_name": provider.name,
            "provider_description": provider.description,
            "provider_address": provider.address,
            "provider_city": provider.city,
            "provider_country": provider.country,
            "provider_country": provider.country,
            "provider_country": provider.country,
            "provider_phone": provider.phone,
            "provider_category": provider.category.name,
            "provider_score": str(provider.score)
        }
        print(registry_detail)
        # Publicar en SQS (provider_append)
        send_message_sqs('provider_append', str(registry_detail))

        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Provider.objects.all()
        provider = get_object_or_404(queryset, pk=pk)
        provider.active = False
        provider.save()

        registry_detail = {
            "id": str(provider.id)
        }
        print(registry_detail)
        # Publicar en SQS (provider_remove)
        send_message_sqs('provider_remove', str(registry_detail))

        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    def retrieve_code(self, request, code):
        queryset = Provider.objects.filter(code=code, active=True)
        provider = get_object_or_404(queryset)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)
