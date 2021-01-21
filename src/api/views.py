from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from api.models import Student
from api.serializers import StudentSerializer


class StudentsResultsPagination(PageNumberPagination):
    page_size = 50

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'next': {
                    'type':
                        'string',
                    'nullable':
                        True,
                    'format':
                        'uri',
                    'example':
                        '/students/?{page_query_param}=4'.format(
                            page_query_param=self.page_query_param)
                },
                'previous': {
                    'type':
                        'string',
                    'nullable':
                        True,
                    'format':
                        'uri',
                    'example':
                        '/students/?{page_query_param}=2'.format(
                            page_query_param=self.page_query_param)
                },
                'results': schema,
            },
        }


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('surname')
    serializer_class = StudentSerializer
    pagination_class = StudentsResultsPagination
    permission_classes = []
