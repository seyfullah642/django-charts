from django.urls import path
from .views import ClubChartView

urlpatterns = [
    path('', ClubChartView.as_view(), name='club_barplot'),
]