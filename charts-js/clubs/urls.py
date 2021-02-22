from django.urls import path
from .views import ClubChartView

urlpatterns = [
    path('club/', ClubChartView.as_view(), name='club_barplot'),
]