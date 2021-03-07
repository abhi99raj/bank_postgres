from bank_details.models import Branches
from bank_details.api.serializers import BranchesSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .mypaginations import MyLimitOffsetPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

class BranchesViewSet(viewsets.ModelViewSet):
 queryset = Branches.objects.all()
 serializer_class = BranchesSerializer
 filter_backends = [DjangoFilterBackend]
 filterset_fields = ['city']
 pagination_class = MyLimitOffsetPagination

class CityViewSet(viewsets.ModelViewSet):
 queryset = Branches.objects.all()
 serializer_class = BranchesSerializer
 filter_backends = [DjangoFilterBackend]
 filterset_fields = ['city']
 search_fields = ['city']


@api_view(['GET'])
def search_ifsc(request):
    if request.method == 'GET':
    	branches = Branches.objects.filter(ifsc=request.GET['ifsc'])
    	serializer = BranchesSerializer(branches, many=True)
    	return Response(serializer.data)
