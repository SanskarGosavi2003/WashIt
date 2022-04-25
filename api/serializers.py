from dataclasses import fields
from rest_framework import serializers
from Washer.models import WashingMachine,Student

class Serializer_Washing_Machine(serializers.ModelSerializer):
    class Meta:
        model = WashingMachine
        fields = '__all__'

class Serializer_Student(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        def update(self,instance,validated_data):
            instance.m_floor = validated_data.get('m_floor',instance.m_floor)
            instance.m_wing = validated_data.get('m_wing',instance.m_wing)
            instance.save()
            return instance
