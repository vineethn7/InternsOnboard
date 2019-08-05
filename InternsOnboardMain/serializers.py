from rest_framework import serializers
from .models import internshipPost

class internshipPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=internshipPost
        fields='__all__'
