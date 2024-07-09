from django.contrib import admin
from hotels_app.models import *

# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'code')

    #pri kreiranje na rezervacija, korisnikot se dodeluva avtomatski spored najaveniot korisnik vo momentot
    #da ne se dozvoli rezerviranje na neiscistena soba
    def save_model(self, request, obj, form, change):
        obj.user = request.user    #object user go dodeluvame da ni bide segasniot korisnik
        if not obj.room.status_Cleaned:
            # You can raise a validation error here or handle it in your preferred way
            raise ValueError("Cannot reserve a room that is not cleaned")

        return super(ReservationAdmin, self).save_model(request, obj, form, change) #go povikuvame konstruktorot na ovoj object i se prakjaat formite

    # da editira samo liceto koe rezervira(user) ili menadzer ili recepcionist
    def has_change_permission(self, request, obj=None):
        if obj:
            if hasattr(obj, 'employee'):
                if obj.employee.type in ['Manager', 'Receptioner']:
                    return obj.user == request.user
        return False


class RoomAdmin(admin.ModelAdmin):
    list_display = ('status_Cleaned', 'r_number')
    #moze da editira soba samo higienicar
    # def has_change_permission(self, request, obj=None):
    #     return obj.user == request.user
    #     # if obj:
    #     #     print(type(obj))
    #     #     if hasattr(obj, 'employee'):
    #     #         if obj.employee.type == "Cleaner":
    #     #             return True
    #     # return False

    #mozhe da dodava soba samo superuser.
    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Employee)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Room, RoomAdmin)