from rest_framework import viewsets
from .serializers import InvestmentSerializer
from .models import Investment


class InvestmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows investments to be viewed or edited
    """
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

