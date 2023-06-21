from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class ProdutorPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'

class ProdutorLOPagination(LimitOffsetPagination):
    default_limit = 1
