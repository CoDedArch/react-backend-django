from customer.models import Customer 
from customer.serializers import CustomerSerializer
from django.http import JsonResponse

def customers(request):
    # handles business logic
    """ query database , serializes request and return response """
    # data that we want to return to the user 
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many = True)
    return JsonResponse({'customers': serializer.data})