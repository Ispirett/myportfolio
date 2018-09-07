from django.shortcuts import render
from django.shortcuts import get_object_or_404
from  rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework  import status
from .models import Stores, StoreOwners, StoreCatagory
from .serializers import StoresSerializer, StoreCatagorySerializer, StoreOwnerSerializer


# get all stores or add new stores
 #class StoreList(APIView):

  #  def get (self,request):
        # get all entries from stores database
      #  stores = Stores.objects.all()
        # take all entries and convert to .json we use many so that we will convert all entries.
      #  serializer = StoresSerializer(stores, many=True)
     #   return Response(serializer.data)

   # def post(self):
     #   pass

# views sets handle get and post request
class StoreView(viewsets.ModelViewSet):
    # get all entries from stores database
    queryset = Stores.objects.all()
    # take all entries and convert to .json we use many so that we will convert all entries.
    serializer_class = StoresSerializer


class StoreCatatgoryView(viewsets.ModelViewSet):
    queryset = StoreCatagory.objects.all()

    serializer_class = StoreCatagorySerializer


class StoreOwnersView(viewsets.ModelViewSet):
    queryset = StoreOwners.objects.all()

    serializer_class = StoreOwnerSerializer