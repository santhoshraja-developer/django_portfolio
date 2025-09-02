from rest_framework import serializers
from .models import Contactmessage

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactmessage
        fields = ['id', 'name', 'email', 'subject', 'message']
