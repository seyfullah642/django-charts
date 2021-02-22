from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
    FacebookConversions,
    AdobeConversions,
    DCMConversions,
)


class ScatterPlotView(TemplateView):
    template_name = 'conversions/conversion_scatterplot.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facebook'] = FacebookConversions.objects.all()
        context['adobe'] = AdobeConversions.objects.all()
        context['dcm'] = DCMConversions.objects.all()
        # print(context['facebook'])
        # print(context['adobe'])
        # print(context['dcm'])
        return context