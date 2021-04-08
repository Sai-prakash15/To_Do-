from rest_framework import pagination

class customPagination(pagination.PageNumberPagination):
    page_size = 5