from django.urls import path
from .views import ScatterPlotView

urlpatterns = [
    path('conversions/', ScatterPlotView.as_view(), name='conversion_scatterplot'),
]