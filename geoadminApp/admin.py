from django.contrib.gis import admin
from .models import Layers, Features
from .forms import FeatureModelForm


# Create a custom admin for the Layers Model
class LayerAdmin(admin.ModelAdmin):
    list_display = ['layername', 'author']
    list_filter = ['author']


admin.site.register(Layers, LayerAdmin)
admin.site.register(Features, admin.GeoModelAdmin)

