from bank_details.models import Branches
from rest_framework import serializers

class BranchesSerializer(serializers.ModelSerializer):
 class Meta:
  model = Branches
  fields = ['ifsc', 'bank_id', 'branch', 'address','city','district','state','bank_name']