from django.utils import timezone
from rest_framework import serializers
from fltapitest.models import User, ActivityPeriod


class DateTimeFieldWihTZ(serializers.DateTimeField):

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)


class ActivityPeriodSerializer(serializers.ModelSerializer):

    start_time = DateTimeFieldWihTZ(format='%b %d %Y %I:%M%p')
    end_time = DateTimeFieldWihTZ(format='%b %d %Y %I:%M%p')

    class Meta:
        model = ActivityPeriod
        fields = ('user', 'start_time', 'end_time')


class UserSerializer(serializers.ModelSerializer):
    tz = serializers.CharField()
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('activityperiod')
    #     user = User.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         ActivityPeriod.objects.create(user=user, **track_data)
    #     return user

