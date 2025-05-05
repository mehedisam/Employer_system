from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ("id", "company_name", "contact_person_name", "email", "phone_number", "address", "created_at")
        read_only_fields = ("id", "created_at")
