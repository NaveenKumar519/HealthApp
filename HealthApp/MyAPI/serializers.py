from rest_framework import serializers
from . models import brain_stroke

class brainStrokeSerializers(serializers.ModelSerializer):
	class Meta:
		model=brain_stroke
		fields='__all__'