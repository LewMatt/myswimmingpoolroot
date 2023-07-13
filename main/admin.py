from django.contrib import admin
from .models import ToDoList, Item, AvailableReservationsTrack, Equipment, Reservation, Work

# Register your models here.

class EquipmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipment._meta.fields]


class ReservationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reservation._meta.fields]

admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(AvailableReservationsTrack)
admin.site.register(Work)
