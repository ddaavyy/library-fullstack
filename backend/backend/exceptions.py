from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and isinstance(exc, Http404):
        response.data = {
            'error': 'Livro não encontrado',
            'detail': str(exc)
        }
        response.status_code = status.HTTP_404_NOT_FOUND

    return response
