from customer.models import Customer 
from customer.serializers import CustomerSerializer
from django.http import JsonResponse, Http404

def customers(request):
    # handles business logic
    """ query database , serializes request and return response """
    # data that we want to return to the user 
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many = True)
    return JsonResponse({'customers': serializer.data})

def customer(request, id):
    try:
      data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
       raise Http404('Customer does not exist')
    serializer = CustomerSerializer(data, many = False)
    return JsonResponse({'customer': serializer.data})

    pass