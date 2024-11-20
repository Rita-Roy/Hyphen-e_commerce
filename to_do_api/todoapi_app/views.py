from rest_framework import viewsets
from .models import Todoitems
from .serializers import    TodoitemsSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset=Todoitems.objects.all()
    serializer_class=   TodoitemsSerializer
# Create your views here.
