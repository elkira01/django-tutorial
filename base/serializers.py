from rest_framework.serializers import ModelSerializer
from .models import Advocate, RentalProperty, Company


class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'


class RentalPropertySerializer(ModelSerializer):
    class Meta:
        model = RentalProperty
        fields = '__all__'

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'