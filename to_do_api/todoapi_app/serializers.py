from rest_framework import serializers    #serializers is the module
from .models import Todoitems

class TodoitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todoitems
        fields=['id','Title','created']