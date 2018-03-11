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

    def retrieve_code(self, request, code):
        queryset = Provider.objects.filter(code=code, active=True)
        offer = get_object_or_404(queryset)
        serializer = ProviderSerializer(offer)
        return Response(serializer.data)
