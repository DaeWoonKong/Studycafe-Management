from django.contrib import admin
from .models import Seat

class SeatAdmin(admin.ModelAdmin):
    search_fields = ['scode']

admin.site.register(Seat, SeatAdmin)