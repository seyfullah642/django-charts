from django.contrib import admin
from .models import (
    FacebookConversions,
    AdobeConversions,
    DCMConversions,)


admin.site.register(FacebookConversions)
admin.site.register(AdobeConversions)
admin.site.register(DCMConversions)

# Register your models here.
