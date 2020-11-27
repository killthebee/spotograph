from django.contrib import admin

from spots.models import Spot, FeatureImage, MainImage, ChatMessage


admin.site.register(Spot)
admin.site.register(FeatureImage)
admin.site.register(MainImage)
admin.site.register(ChatMessage)