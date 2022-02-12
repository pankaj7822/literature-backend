import datetime
from rest_framework.response import Response
from core.models import Literature
from core.serializers import LiteratureSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def literature_list(request):
    """
    Lists all Literature.
    """
    literatures = Literature.objects.all()
    serializer = LiteratureSerializer(literatures, many=True)
    return Response(serializer.data)

