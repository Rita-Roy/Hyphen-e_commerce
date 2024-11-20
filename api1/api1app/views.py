from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product



@api_view(['GET'])
def api_overview(request):
    api_urls={
        'List': '/product-list/',
        'Single Product view': '/product-view/<int:id>',
        'create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>'
    }
    return Response(api_urls)

@api_view(['POST'])
def Createproduct(request):
    prod=ProductSerializer(data=request.data)  #deserialization
    if prod.is_valid():
        prod.save()
    return Response("Created")


@api_view(['GET'])
def showall(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)  #serialization
    return Response(serializer.data)



#single product view
@api_view(['GET'])
def singleprodview(request,pk):
    products=Product.objects.get(id=pk)
    serializer=ProductSerializer(products,many=False)
    return Response(serializer.data)

#partial update
@api_view(['PATCH'])
def Updateproductpartial(request,pk):
    product=Product.objects.get(id=pk)
    if request.method=='PATCH':
        serializer=ProductSerializer(instance=product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def Deleteproduct(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return Response('deleted')

    