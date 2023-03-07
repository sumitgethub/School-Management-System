from Master.models import Gender 
from rest_framework import serializers

class GenderMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = "__all__"      