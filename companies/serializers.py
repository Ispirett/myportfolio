from rest_framework import serializers
from companies.models import Stores, StoreCatagory, StoreOwners

class StoresSerializer (serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stores
        fields = '__all__'



class StoreCatagorySerializer(serializers.HyperlinkedModelSerializer):

     class Meta:
         model = StoreCatagory
         fields = '__all__'




class StoreOwnerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StoreOwners
        fields = '__all__'