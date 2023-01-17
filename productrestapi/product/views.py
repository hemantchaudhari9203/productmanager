from django.shortcuts import render
from django.http import JsonResponse
from .models import product
from .serializer import productserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,permissions,authentication
from rest_framework import generics, mixins
from .permission import employee_permissions
# Create your views here.


# function based view
@api_view(['GET','POST'])
def product_list(request,format=None):
    if request.method=='GET':
        prod_data=product.objects.all()
        serializer_prod=productserializer(prod_data,many=True)
        return JsonResponse({'data':serializer_prod.data})
    if request.method=='POST':
        serializer_prod=productserializer(data=request.data)
        if serializer_prod.is_valid():
            serializer_prod.save()
        return Response(serializer_prod.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def product_URD(request, id, format=None):
    try:
        prod_data=product.objects.get(id=id)
    except prod_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serialize_prod=productserializer(prod_data)
        return Response(serialize_prod.data)
    elif request.method=='PUT':
        serialize_prod=productserializer(prod_data,data=request.data)
        if serialize_prod.is_valid():
            serialize_prod.save()
            return Response(serialize_prod.data)
        return Response(serialize_prod.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        prod_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class based view
class product_mixin_listcreate(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
    ):
    queryset=product.objects.all()
    serializer_class=productserializer
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes = [employee_permissions]#[permissions.IsAuthenticated]


    def get(self,request,*args,**kwargs):

        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class product_mixin_retriveupdatedelete(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
    ):
    queryset=product.objects.all()
    serializer_class=productserializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[authentication.SessionAuthentication]
    lookup_field="pk"
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args, **kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args, **kwargs)



# admin admin@123

# https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views