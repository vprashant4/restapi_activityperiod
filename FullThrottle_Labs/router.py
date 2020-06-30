from fltapitest.api.viewsets import UserViewSets#, ActivityPeriodViewSets
from rest_framework import routers

routers = routers.DefaultRouter()
#routers.register('useractiveperiod', ActivityPeriodViewSets, basename='useractiveperiod')
routers.register('user', UserViewSets, basename='user')
