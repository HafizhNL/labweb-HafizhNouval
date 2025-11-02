from rest_framework import serializers
from basic_api.models import DRFPost, DRFDosen, DRFStudent

class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPost
        fields = '__all__'

class DRFPostDosenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFDosen
        fields = '__all__'

class DRFPostStudentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = DRFStudent
        fields = '__all__'