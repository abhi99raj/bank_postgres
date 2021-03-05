from bank_details.models import Branches
from bank_details.api.serializers import BranchesSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .mypaginations import MyLimitOffsetPagination

class BranchesViewSet(viewsets.ModelViewSet):
 queryset = Branches.objects.all()
 serializer_class = BranchesSerializer
 filter_backends = [DjangoFilterBackend]
 filterset_fields = ['city']
 pagination_class = MyLimitOffsetPagination
