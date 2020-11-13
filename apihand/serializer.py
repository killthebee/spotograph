from rest_framework import serializers

from spots.models import Spot
from apihand.services import valid_coord


class SpotDetailSerializer(serializers.ModelSerializer):
    """
    validate spot text data
    """
    def validate_latitude(self, value):
        if not valid_coord(value):
            raise serializers.ValidationError("Error")
        else:
            return value

    def validate_longitude(self, value):
        if not valid_coord(value):
            raise serializers.ValidationError("Error")
        else:
            return value

    class Meta:
        model = Spot
        exclude = ('owner', )