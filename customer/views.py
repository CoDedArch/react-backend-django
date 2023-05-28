from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customers(request):
    # handles business logic
    """ query database , serializes request and return response """
    # data that we want to return to the user 
    if request.method == 'GET':
      data = Customer.objects.all()
      serializer = CustomerSerializer(data, many = True)
      return Response({'customers': serializer.data})
    
    elif request.method == 'POST':
       serializer = CustomerSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def customer(request, id):
    try:
      data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
      serializer = CustomerSerializer(data, many = False)
      return Response({'customer': serializer.data})
    elif request.method == 'DELETE':
       data.delete()
       return Response('data has been deleted', status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
       serializer = CustomerSerializer(data, data= request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'customer':serializer.data})
       return Response(serializer.errors, statu=status.HTTP_400_BAD_REQUEST)

    pass