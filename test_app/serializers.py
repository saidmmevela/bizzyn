from rest_framework import serializers
from .models import TestModel, UserModel

# class SimpleObject():
#     def __init__(self, name):
#         self.name = name

# class SimpleObjectSerializer(serializers.Serializer):
class SimpleObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields ="__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields ="__all__"
    # name = serializers.CharField()
    # description = serializers.CharField()
    # phone_number = serializers.IntegerField()
    # is_live = serializers.BooleanField()
    # amount = serializers.FloatField()
    # created_at =serializers.DateTimeField(read_only=True)
    # updated_at =serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     return TestModel.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     TestModel.objects.filter(id=instance.id).update(**validated_data)
    #     return TestModel.objects.get(id=instance.id)

# def run_data():
#     simple_var = SimpleObject("Henry")
#     simple_var_serializer = SimpleObjectSerializer(simple_var)
#     print(simple_var_serializer.data)