
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import FoodDatas, KitoStandard
from .serializer import FoodSerializer, KitoSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import filters
from rest_framework.response import Response
from django.db.models import Count
from users.models import User
from rest_framework.decorators import api_view


class OwnPagination(PageNumberPagination):
    page_size = 10

class KitoStandardView(APIView):
    def get(self, request):
        Kito = KitoStandard.objects.all()
        serializer = KitoSerializer(Kito, many=True, context={"request": request})
        return Response(serializer.data)
    
class ListFoodsView(APIView):
    def get(self, request):
        paginator = OwnPagination()
        foods = FoodDatas.objects.all()
        results = paginator.paginate_queryset(foods, request)
        serializer = FoodSerializer(results, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)
@api_view(["GET"])
def food_search(request):
    paginator = OwnPagination()
    pd_name = request.GET.get("pd_name", None)
    date = request.GET.get("date", None)
    filter_kwargs = {}
    if pd_name is not None:
        filter_kwargs["PRDLST_NM__icontains"] = pd_name
    if date is not None:
        filter_kwargs["PRDLST_REPORT_NO__gte"] = date
    try:
        foods = FoodDatas.objects.filter(**filter_kwargs).order_by('-PRDLST_REPORT_NO', 'PRDLST_NM')
    except ValueError:
        foods = FoodDatas.objects.all()
    results = paginator.paginate_queryset(foods, request)
    serializer = FoodSerializer(results, many=True,context={"request": request})
    return paginator.get_paginated_response(serializer.data)

@api_view(["GET"])
def kito_search(request):
    paginator = OwnPagination()
    name = request.GET.get("name", None)
    filter_kwargs = {}
    if name is not None:
        filter_kwargs["RW_NAME__icontains"] = name

    try:
        kit = KitoStandard.objects.filter(**filter_kwargs).order_by('RW_NAME')
    except ValueError:
        kit = KitoStandard.objects.all()
    results = paginator.paginate_queryset(kit, request)
    serializer = KitoSerializer(results, many=True,context={"request": request})
    return paginator.get_paginated_response(serializer.data)

