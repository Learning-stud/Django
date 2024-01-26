from rest_framework import  serializers
from .models import *

class StudentSerializers(serializers.ModelSerializers):
  class Meta:
    models = Students
    fields = ("id","firstname","lastname")