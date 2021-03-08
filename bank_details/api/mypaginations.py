from rest_framework.pagination import PageNumberPagination

class MyLimitOffsetPagination(PageNumberPagination):
 page_size = 5
 
 