from django.contrib import admin

from workshop.models import Topic, Workshop


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    pass
