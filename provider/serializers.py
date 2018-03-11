from rest_framework import serializers

from .models import (Category, Requirement, Provider, Support, Calification)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class RequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requirement
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        fields = '__all__'


class CalificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calification
        fields = '__all__'
