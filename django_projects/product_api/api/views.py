from rest_framework.decorators import api_view
from api import models, serializers
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    products = models.Product.objects.all()
    serializer = serializers.ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def ProductDetail(request,pk):
    product = models.Product.objects.get(id=pk)
    serializer = serializers.ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def AddProduct(request):
    serializer = serializers.ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request,pk):
    product = models.Product.objects.get(id=pk)
    serializer = serializers.ProductSerializer(instance= product, data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def Deleteproduct(request,pk):
    product = models.Product.objects.get(id=pk)
    product.delete()

    return Response('Product deleted Successfully')                    