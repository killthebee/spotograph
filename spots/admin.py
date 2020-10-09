from django.contrib import admin

from spots.models import Spot, FeatureImage, MainImage


admin.site.register(Spot)
admin.site.register(FeatureImage)
admin.site.register(MainImage)