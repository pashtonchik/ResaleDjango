import json
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.files import File
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orderlist.models import Order


@api_view(['POST'])
def create_order(request):
    try:
        order_info = json.loads(request.body.decode("utf-8"))
        order = Order(
            size=order_info['size'],
            contact=order_info['contact'],
        )
        order.save()

        print(order.size)
        photo = File(open(f"orders_images/{order_info['image']}", 'rb'))
        order.image = photo
        order.save()
        return Response(status=status.HTTP_200_OK)
    except ValidationError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)