from fltapitest.api.serializers import UserSerializer, ActivityPeriodSerializer
from fltapitest.models import ActivityPeriod, User
from rest_framework import viewsets


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityPeriodViewSets(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer





