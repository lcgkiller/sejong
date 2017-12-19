from rest_framework import serializers

from .models import Credit


class CreditSerializer(serializers.ModelSerializer):

    data = serializers.JSONField()

    class Meta:
        model = Credit
        fields = (
            'id',
            'admission_year',
            'college',
            'department',
            'core_essential',
            'core_essential_selection',
            'major_basic',
            'sum_of_major',
            'major_required',
            'major_select',
            'sum_of_all'
        )


