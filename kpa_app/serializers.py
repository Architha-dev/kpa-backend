from rest_framework import serializers
from .models import WheelSpecification, WheelSpecificationSubmission

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'


class WheelSpecificationSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecificationSubmission
        fields = '__all__'