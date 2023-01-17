from rest_framework import serializers
from .models import product
class productserializer(serializers.ModelSerializer):
    # pname=serializers.CharField(max_length=30,required=True)
    # pvendor=serializers.CharField(max_length=30,required=True)
    # pmodel=serializers.CharField(max_length=30, required=True)
    # pqty=serializers.IntegerField()
    # pprice=serializers.FloatField()
    class Meta:
        model=product
        fields='__all__'


